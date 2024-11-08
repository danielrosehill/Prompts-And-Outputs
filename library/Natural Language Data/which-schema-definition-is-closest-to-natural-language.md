---
title: "Which schema definition is closest to natural language"
---
![GPT-4o](https://img.shields.io/badge/GPT--4o-3333FF?style=for-the-badge&logo=openai&logoColor=white)



*Note: this repository consists of the outputs of large language models (LLMs). In many cases, these are unedited or minimally edited. The information provided is for demonstrative purposes only and is intended to highlight constraints and capabilities in LLM applications and prompt engineering strategies.*


# Prompt

Which ORM that is compatible with Postgres has the language for defining the schema that is the closest approximation to written text?

# Output

from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='posts')

    def __repr__(self):
        return f"<Post(title={self.title}, content={self.content[:20]})>"

User.posts = relationship('Post', order_by=Post.id, back_populates='user')

# Create an engine and the schema
engine = create_engine('postgresql://username:password@localhost/mydatabase')
Base.metadata.create_all(engine)## Extracted Prompts
[[Prompts/Autocapture/Which schema definition is closest to natural language.md#Prompt 1|Prompt 1]]





## Extracted Prompts
[[Prompts/Which schema definition is closest to natural language.md#Prompt 1|Prompt 1]]
