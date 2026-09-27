"""add patients table

Revision ID: b5c9d8e7f6a1
Revises: 03a26cc7d7b0
Create Date: 2026-08-31

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5c9d8e7f6a1'
down_revision: Union[str, Sequence[str], None] = '03a26cc7d7b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema: create patients table."""
    op.create_table(
        'patients',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('Name', sa.String(length=25), nullable=True),
        sa.Column('Pregnancies', sa.Integer(), nullable=True),
        sa.Column('Glucose', sa.Integer(), nullable=False),
        sa.Column('BloodPressure', sa.Integer(), nullable=False),
        sa.Column('SkinThickness', sa.Integer(), nullable=False),
        sa.Column('Insulin', sa.Integer(), nullable=True),
        sa.Column('Bmi', sa.Float(), nullable=False),
        sa.Column('DiabetesPedigreeFunction', sa.Float(), nullable=True),
        sa.Column('Age', sa.Integer(), nullable=False),
        sa.Column('Diabetic', sa.Boolean(), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema: drop patients table."""
    op.drop_table('patients')
