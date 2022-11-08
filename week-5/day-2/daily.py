class Pagination:

    FIRST_PAGE = 1
    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = int(pageSize)
        self.page = self.FIRST_PAGE
        totalPages = len(self.items) / self.pageSize
        if not totalPages.is_integer():
            totalPages += 1
        self.totalPages = int(totalPages)
    def getVisibleItems(self):
        start = (self.page - 1) * self.pageSize
        end = self.page * self.pageSize
        return self.items[start:end]
    def prevPage(self):
        if self.page == self.FIRST_PAGE:
            return self
        self.page -= 1
        return self
    def nextPage(self):
        if self.page == self.totalPages:
            return self
        self.page += 1
        return self
    def firstPage(self):
        self.page = self.totalPages
        return self
    def lastPage(self):
        self.page = self.totalPages
        return self
    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        if pageNum > self.totalPages:
            pageNum = self.totalPages
        elif pageNum < self.FIRST_PAGE:
            pageNum = self.FIRST_PAGE
        self.page = pageNum

    def main():
        alphabetList = list("abcdefghijklmnopqrstuvwxyz")
        p = Pagination(alphabetList, 4)
        p.lastPage()
        print(p.getVisibleItems())
        p.prevPage()
        print(p.getVisibleItems())
        p.prevPage()
        print(p.getVisibleItems())
        p.goToPage(4)
        print(p.getVisibleItems())
        p.goToPage(-1)
        print(p.getVisibleItems())
        p.goToPage(22)
        print(p.getVisibleItems())
        p.prevPage().prevPage().nextPage()
        print(p.getVisibleItems())
main()