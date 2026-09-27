from database import Base, engine


def main():
    """Create all tables from SQLAlchemy models (quick, non-migration method)."""
    Base.metadata.create_all(bind=engine)
    print("Tables created (if not existing).")


if __name__ == "__main__":
    main()
