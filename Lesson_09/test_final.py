"""
Three CRUD tests for subject table + PRIMARY KEY test
Simple version, all in one file
"""

import pytest
from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.orm import sessionmaker, declarative_base

# Database setup
DATABASE_URL = "postgresql://postgres:12345@localhost:5432/QA"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Subject(Base):
    """Subject model"""
    __tablename__ = 'subject'
    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String)

    def __repr__(self):
        return f"<Subject(id={self.subject_id}, title='{self.subject_title}')>"


# Create table
Base.metadata.create_all(engine)


# ============ TEST 1: CREATE ============
def test_create_subject():
    """Test subject creation (CREATE)"""
    session = Session()
    
    # 1. Clean before test
    session.query(Subject).filter_by(subject_id=101).delete()
    session.commit()
    
    # 2. Create subject
    subject = Subject(subject_id=101, subject_title="Mathematics")
    session.add(subject)
    session.commit()
    
    # 3. Verify
    saved = session.query(Subject).filter_by(subject_id=101).first()
    assert saved is not None, "Subject was not saved in DB"
    assert saved.subject_title == "Mathematics", "Subject title doesn't match"
    
    print("✅ TEST 1: Subject created successfully")
    
    # 4. Clean after test
    session.delete(saved)
    session.commit()
    session.close()


# ============ TEST 2: UPDATE ============
def test_update_subject():
    """Test subject update (UPDATE)"""
    session = Session()
    
    # 1. Clean before test
    session.query(Subject).filter_by(subject_id=102).delete()
    session.commit()
    
    # 2. Create subject
    subject = Subject(subject_id=102, subject_title="Physics")
    session.add(subject)
    session.commit()
    
    # 3. Update
    subject.subject_title = "Advanced Physics"
    session.commit()
    
    # 4. Verify
    updated = session.query(Subject).filter_by(subject_id=102).first()
    assert updated is not None, "Subject not found after update"
    assert updated.subject_title == "Advanced Physics", "Title was not updated"
    
    print("✅ TEST 2: Subject updated successfully")
    
    # 5. Clean after test
    session.delete(updated)
    session.commit()
    session.close()


# ============ TEST 3: DELETE ============
def test_delete_subject():
    """Test subject deletion (DELETE)"""
    session = Session()
    
    # 1. Clean before test
    session.query(Subject).filter_by(subject_id=103).delete()
    session.commit()
    
    # 2. Create subject
    subject = Subject(subject_id=103, subject_title="Chemistry")
    session.add(subject)
    session.commit()
    
    # 3. Delete
    session.delete(subject)
    session.commit()
    
    # 4. Verify
    deleted = session.query(Subject).filter_by(subject_id=103).first()
    assert deleted is None, "Subject should be deleted from DB"
    
    print("✅ TEST 3: Subject deleted successfully")
    session.close()


# ============ TEST 4: PRIMARY KEY UNIQUENESS ============
def test_primary_key_uniqueness():
    """Test that subject_id is defined as PRIMARY KEY in model"""
    session = Session()
    
    # Clean before test
    session.query(Subject).filter_by(subject_id=104).delete()
    session.commit()
    
    # Check that subject_id is primary key
    mapper = inspect(Subject)
    primary_key_columns = [col.name for col in mapper.primary_key]
    
    assert "subject_id" in primary_key_columns, \
        "subject_id should be defined as PRIMARY KEY in model"
    
    # Create subject
    subject = Subject(subject_id=104, subject_title="Biology")
    session.add(subject)
    session.commit()
    
    # Verify it was saved
    saved = session.query(Subject).filter_by(subject_id=104).first()
    assert saved is not None, "Subject should be saved"
    assert saved.subject_id == 104, "ID should match"
    
    print("✅ TEST 4: PRIMARY KEY correctly defined in model")
    
    # Clean after test
    session.delete(saved)
    session.commit()
    session.close()


