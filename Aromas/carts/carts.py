class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart
    
    def saveCart(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def addProduct(self, product):
        id = str(product.id)
        pic = str(product.thumbnail)
        if id not in self.cart.keys():
            self.cart[id]={"product_id": product.id, "qty": 1, "pic":pic, "title":product.title, "total": product.price}
        else:
            self.cart[id]["qty"] += 1
            self.cart[id]["total"] = self.cart[id]["qty"] * product.price
        self.saveCart()

    def deleteProductCart(self, product):
        id = str(product.id)
        if id in self.cart:
            del self.cart[id]
            self.saveCart()
    
    def decreaseProduct(self, product):
        id = str(product.id)
        if id in self.cart.keys():
            self.cart[id]["qty"] -= 1
            self.cart[id]["total"] = self.cart[id]["qty"] * product.price
            if self.cart[id]["qty"] <= 0: self.deleteProductCart(product)
        self.saveCart()

    def emptyCart(self):
        self.session["cart"] = {}
        self.session.modified = True



