# from sqlalchemy.orm import Session
# import models, schemas

# def get_item(db: Session, item_id: int):
#     return db.query(models.Pdf).filter(models.Pdf.id == item_id).first()

# # def get_items(db: Session, skip: int = 0, limit: int = 10):
# #     return db.query(models.Pdf).offset(skip).limit(limit).all()

# def create_item(db: Session, item: schemas.Item):
#     db_item = models.Pdf(file_name=item.file_name, upload_date=item.upload_date)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
