class Pagination:
    def __init__(self,cursor=None):
        self.cursor = cursor

    def get(self,offset,per_page,no_pages):
        offset,per_page,no_pages=int(offset),int(per_page),int(no_pages)
        skip = offset * per_page
        limit = no_pages * per_page
        self.cursor = self.cursor.skip(skip).limit(limit)
        return self.cursor

    def count(self):
        return self.cursor.count()
