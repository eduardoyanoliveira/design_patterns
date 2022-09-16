from modules.leaf import ProductLeaf
from modules.composite import ProductComposite


if __name__ == '__main__':
    
    playstation_5 = ProductLeaf('PlayStation 5', 700)
    smartphone = ProductLeaf('Smartphone', 500)
    xbox_series_x = ProductLeaf('Xbox series X', 500)
    
    product_container = ProductComposite()
    product_container.add(playstation_5, smartphone, xbox_series_x)

    tablet = ProductLeaf('Tablet', 300)
    head_phone = ProductLeaf('HeadPhone', 200)
    second_product_container = ProductComposite()
    second_product_container.add(tablet, head_phone)
    product_container.add(second_product_container)

    print(product_container)
    print(product_container.get_quantity())
    