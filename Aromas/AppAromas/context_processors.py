def lengthCart(request):
    if request.session.get("cart"):
        lCart = len(request.session.get("cart"))
    else:
        lCart = 0
    return(lCart)

def totalCart(request):
    if request.session.get("cart"):
        tCart = 0
        cart = request.session.get("cart")
        for item in cart:
            tCart = tCart + int(cart[item]['total'])
    else:
        tCart = 0
    return(tCart)



def mis_variables(request):
    lCart = lengthCart(request)
    tCart = totalCart(request)
    return {"lengthCart": lCart, "totalCart": tCart}

