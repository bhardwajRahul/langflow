"""Fix Credential table

Revision ID: fd531f8868b1
Revises: 2ac71eb9c3ae
Create Date: 2023-11-24 15:07:37.566516

"""

from typing import Optional, Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.engine.reflection import Inspector

# revision identifiers, used by Alembic.
revision: str = "fd531f8868b1"
down_revision: Union[str, None] = "2ac71eb9c3ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    inspector = sa.inspect(conn)  # type: ignore
    tables = inspector.get_table_names()
    foreign_keys_names = []
    if "credential" in tables:
        foreign_keys = inspector.get_foreign_keys("credential")
        foreign_keys_names = [fk["name"] for fk in foreign_keys]

    try:
        if "credential" in tables and "fk_credential_user_id" not in foreign_keys_names:
            with op.batch_alter_table("credential", schema=None) as batch_op:
                batch_op.create_foreign_key("fk_credential_user_id", "user", ["user_id"], ["id"])
    except Exception as e:
        print(e)
        pass

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    conn = op.get_bind()
    inspector = sa.inspect(conn)  # type: ignore
    tables = inspector.get_table_names()
    foreign_keys_names: list[Optional[str]] = []
    if "credential" in tables:
        foreign_keys = inspector.get_foreign_keys("credential")
        foreign_keys_names = [fk["name"] for fk in foreign_keys]
    try:
        if "credential" in tables and "fk_credential_user_id" in foreign_keys_names:
            with op.batch_alter_table("credential", schema=None) as batch_op:
                batch_op.drop_constraint("fk_credential_user_id", type_="foreignkey")
    except Exception as e:
        print(e)
        pass

    # ### end Alembic commands ###
