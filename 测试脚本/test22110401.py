from unittest import TestCase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# global application scope.  create Session class, engine
Session = sessionmaker()

engine = create_engine('postgresql://...')


class SomeTest(TestCase):
    def setUp(self):
        # connect to the database
        self.connection = engine.connect()

        # begin a non-ORM transaction
        self.trans = self.connection.begin()

        # bind an individual Session to the connection
        self.session = Session(bind=self.connection)

        ###    optional     ###

        # if the database supports SAVEPOINT (SQLite needs special
        # config for this to work), starting a savepoint
        # will allow tests to also use rollback within tests

        self.nested = self.connection.begin_nested()

        @event.listens_for(self.session, "after_transaction_end")
        def end_savepoint(session, transaction):
            if not self.nested.is_active:
                self.nested = self.connection.begin_nested()

        ### ^^^ optional ^^^ ###

    def test_something(self):
        # use the session in tests.

        self.session.add(Foo())
        self.session.commit()

    def test_something_with_rollbacks(self):
        # if the SAVEPOINT steps are taken, then a test can also
        # use session.rollback() and continue working with the database

        self.session.add(Bar())
        self.session.flush()
        self.session.rollback()

        self.session.add(Foo())
        self.session.commit()

    def tearDown(self):
        self.session.close()

        # rollback - everything that happened with the
        # Session above (including calls to commit())
        # is rolled back.
        self.trans.rollback()

        # return connection to the Engine
        self.connection.close()
