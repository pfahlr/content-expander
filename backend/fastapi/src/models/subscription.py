from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class Subscription(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    user_id: int = Field(foreign_key="user.id")

    # 🔄 General status
    status: str = Field(default="incomplete", max_length=50)  # active, expired, cancelled, etc.

    # 🧾 Payment gateway info
    provider: str = Field(default="stripe", max_length=50)  # stripe, coinbase, btcpay, etc.
    subscription_type: str = Field(default="recurring", max_length=50)  # recurring, one-time, donation

    # 💳 Common identifiers
    product_id: Optional[str] = Field(default=None, max_length=100)
    price_id: Optional[str] = Field(default=None, max_length=100)
    external_customer_id: Optional[str] = Field(default=None, max_length=100)
    external_subscription_id: Optional[str] = Field(default=None, max_length=100)

    # 🧠 Crypto-specific
    crypto_wallet_address: Optional[str] = Field(default=None, max_length=255)
    crypto_tx_id: Optional[str] = Field(default=None, max_length=255)
    crypto_network: Optional[str] = Field(default=None, max_length=50)  # BTC, ETH, Lightning, etc.

    # 📆 Periods
    current_period_start: Optional[datetime] = None
    current_period_end: Optional[datetime] = None
    cancel_at_period_end: Optional[bool] = False

    # ⏱ Audit fields
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)