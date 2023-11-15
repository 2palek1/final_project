"""azure migration

Revision ID: 06d5986e4bfe
Revises: 
Create Date: 2023-11-15 21:04:01.403039

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06d5986e4bfe'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unit_number', sa.String(), nullable=True),
    sa.Column('street_number', sa.String(), nullable=False),
    sa.Column('address_line1', sa.String(), nullable=False),
    sa.Column('address_line2', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('region', sa.String(), nullable=False),
    sa.Column('postal_code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('permissions', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_address',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('product_image', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['product_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('variation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['product_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('SKU', sa.Integer(), nullable=False),
    sa.Column('qty_in_stock', sa.Integer(), nullable=False),
    sa.Column('product_image', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('variation_option',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('variation_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['variation_id'], ['variation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_configuration',
    sa.Column('product_item_id', sa.Integer(), nullable=True),
    sa.Column('variation_option_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_item_id'], ['product_item.id'], ),
    sa.ForeignKeyConstraint(['variation_option_id'], ['variation_option.id'], )
    )
    op.create_table('shopping_cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shopping_cart_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('product_item_id', sa.Integer(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['shopping_cart.id'], ),
    sa.ForeignKeyConstraint(['product_item_id'], ['product_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_payment_method',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('payment_type_id', sa.Integer(), nullable=True),
    sa.Column('provider', sa.String(), nullable=False),
    sa.Column('account_number', sa.String(), nullable=False),
    sa.Column('expire_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('is_default', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['payment_type_id'], ['payment_type.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shipping_method',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shop_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('order_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('payment_method_id', sa.Integer(), nullable=True),
    sa.Column('shipping_address', sa.Integer(), nullable=True),
    sa.Column('shipping_method', sa.Integer(), nullable=True),
    sa.Column('order_total', sa.Integer(), nullable=False),
    sa.Column('order_status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_status'], ['order_status.id'], ),
    sa.ForeignKeyConstraint(['payment_method_id'], ['user_payment_method.id'], ),
    sa.ForeignKeyConstraint(['shipping_address'], ['address.id'], ),
    sa.ForeignKeyConstraint(['shipping_method'], ['shipping_method.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop_order')
    op.drop_table('shipping_method')
    op.drop_table('order_status')
    op.drop_table('user_payment_method')
    op.drop_table('payment_type')
    op.drop_table('shopping_cart_item')
    op.drop_table('shopping_cart')
    op.drop_table('product_configuration')
    op.drop_table('variation_option')
    op.drop_table('product_item')
    op.drop_table('variation')
    op.drop_table('product')
    op.drop_table('product_category')
    op.drop_table('user_address')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('address')
    # ### end Alembic commands ###
