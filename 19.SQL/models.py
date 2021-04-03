#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, CHAR, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(CHAR(20), primary_key = True)
    name = Column(CHAR(20))

class Solary(Base):
    __tablename__ = 'solary'

    id = Column(INTEGER, primary_key = True)
    name = Column(CHAR(20))
    num = Column(CHAR(20))