class Cart {
    var products = [];

    function addToCart(product) {
        products.push(product);
    }

    constructor(products) {
        this.innerIndex = 0;
        this.products = products;
    }

    // To iterate over every product in the user's cart.
    [Symbol.iterator]() {
        return {
            next: () => {
                if (this.innerIndex < this.products.length) {
                    return {value: this.products[this.innerIndex++],
                            done: false};
                } else {
                    this.innerIndex = 0;
                    // If we would like to iterate over this again without
                    // forcing manual update of the index
                    return {done: true};
                }
            }
        }
    }

}

module.exports('cart');
