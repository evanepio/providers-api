from sqlmodel import Field, SQLModel, UniqueConstraint


class Company(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    slug: str
    slogan: str

    __table_args__ = (
        UniqueConstraint("name"),
        UniqueConstraint("slug"),
    )

    def __repr__(self):
        return f"{self.__name__}(id={self.id!r}, name={self.name!r})"


class CompanyCreate(SQLModel):
    name: str
    slug: str
    slogan: str


class CompanyRead(SQLModel):
    id: int
    name: str
    slug: str
    slogan: str
