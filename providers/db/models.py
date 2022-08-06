from sqlmodel import Field, SQLModel, UniqueConstraint


class CompanyBase(SQLModel):
    name: str
    slug: str
    slogan: str


class Company(CompanyBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    __table_args__ = (
        UniqueConstraint("name"),
        UniqueConstraint("slug"),
    )


class CompanyCreate(CompanyBase):
    pass


class CompanyRead(CompanyBase):
    id: int


class CompanyUpdate(SQLModel):
    name: str | None
    slug: str | None
    slogan: str | None
