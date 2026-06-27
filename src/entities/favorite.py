from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Favorite(Base):
    __tablename__ = "favorite"

    id_favorite = Column(Integer, primary_key=True, autoincrement=True)
    id_eleve    = Column(Integer, ForeignKey("eleve.id_eleve"), nullable=False)
    id_produit  = Column(Integer, ForeignKey("produit.id_produit"), nullable=False)
    date_ajout  = Column(DateTime, default=datetime.now)
    note        = Column(Float, nullable=True)  # note de 1 à 5

    def __repr__(self):
        return f"<Favorite(id={self.id_favorite}, eleve={self.id_eleve}, produit={self.id_produit}, note={self.note})>"