class Product
{
    var name, sku;

    function Product(name, sku) {
        this.name = name;
        this.sku = sku;
    }

    function renderHTML() {
        return '<div class="product"><li>'+ this.name +
               '<button class="add-item">Add to Cart</button></li></div>';
    }
}
