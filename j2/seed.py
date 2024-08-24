from app import create_app, db
from app.models import ProductGroup, Product

app = create_app()

with app.app_context():
    # Create categories
    categories = [
        ProductGroup(product_group_name="Ready-Made Meals", description="Convenient meals that are easy to prepare or eat on the go."),
        ProductGroup(product_group_name="Snacks", description="A selection of popular snacks for any time of the day."),
        ProductGroup(product_group_name="Beverages", description="A range of popular drinks including sodas, juices, and energy drinks."),
        ProductGroup(product_group_name="Desserts", description="Sweet treats and desserts that are easy to enjoy."),
        ProductGroup(product_group_name="Pantry Staples", description="Essential items for everyday cooking and baking."),
        ProductGroup(product_group_name="Frozen Foods", description="A variety of frozen items for easy meals."),
    ]

    # Add categories to the session
    for category in categories:
        db.session.add(category)

    # Commit categories to the database
    db.session.commit()

    # Create products
    products = [
        # Ready-Made Meals
        Product(product_name="Frozen Pizza", price=10, image_url="https://i5.walmartimages.com/asr/35e0da52-6725-4e7c-99f6-f8269ef10dfb.6d81351dcb3479dd84dd8134890f3190.jpeg", description="Delicious and easy-to-bake pizza, perfect for quick meals at home.", product_group_id=1),
        Product(product_name="Pre-Cooked Chicken Breasts", price=12, image_url="https://th.bing.com/th/id/R.8d0056c0597aff31e08ca28e513acf56?rik=ZirUYjnFWRYJ6g&pid=ImgRaw&r=0", description="Tender and flavorful, ready-to-eat chicken for a fast, protein-packed meal.", product_group_id=1),
        Product(product_name="Instant Noodles", price=5, image_url="https://th.bing.com/th/id/OIP.vdi_w2DUVDsv1EY1vHfDgAHaIc?rs=1&pid=ImgDetMain", description="Quick and tasty noodles, ready in minutes for a satisfying meal.", product_group_id=1),

        # Snacks
        Product(product_name="Potato Chips", price=3, image_url="https://th.bing.com/th/id/OIP.ZH4G4XePdtxANzvjewwIbQHaE7?rs=1&pid=ImgDetMain", description="Crispy, salty, and addictive potato chips for anytime snacking.", product_group_id=2),
        Product(product_name="Granola Bars", price=4, image_url="https://th.bing.com/th/id/OIP.hPDy-tsM4s_gi0dEZFVWGQHaLG?rs=1&pid=ImgDetMain", description="Nutritious and delicious bars, great for on-the-go energy.", product_group_id=2),
        Product(product_name="Mixed Nuts", price=6, image_url="https://th.bing.com/th/id/OIP.HvnsFcaEaPBQ3wtXZqn1FgAAAA?rs=1&pid=ImgDetMain", description="A healthy mix of crunchy nuts, perfect for a quick snack.", product_group_id=2),

        # Beverages
        Product(product_name="Cola", price=2, image_url="https://th.bing.com/th?id=OSK.HERORAhs2FjivZzE8Xe9mkl-CBMtlalcWqBWgraUJIvYImw&w=312&h=200&c=15&rs=2&o=6&dpr=1.3&pid=SANGAM", description="Classic, refreshing cola to quench your thirst.", product_group_id=3),
        Product(product_name="Orange Juice", price=4, image_url="https://th.bing.com/th/id/OIP.jqxR_QrdtXQR6kfXBUHrBAHaFD?w=218&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7", description="Fresh and zesty orange juice packed with vitamins.", product_group_id=3),
        Product(product_name="Energy Drinks", price=3, image_url="https://th.bing.com/th/id/OIP.kntu4XmWrZLy0ZqTw7YPwgAAAA?w=254&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7", description="Boost your energy with a burst of flavor and vitality.", product_group_id=3),

        # Desserts
        Product(product_name="Ice Cream", price=5, image_url="https://th.bing.com/th/id/OIP.lFEzsOjEyZLb9hK-N-CKeQHaE8?w=233&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7", description="Creamy and delightful ice cream for a sweet treat.", product_group_id=4),
        Product(product_name="Cookies", price=4, image_url="https://th.bing.com/th/id/OIP.59Y4u1n3EPLiTUnBLtJKjAHaE8?w=282&h=188&c=7&r=0&o=5&dpr=1.3&pid=1.7", description="Soft and chewy cookies baked to perfection.", product_group_id=4),
        Product(product_name="Brownies", price=6, image_url="https://th.bing.com/th/id/R.0484fd90c72a6ae8e750d40f8221b3b9?rik=8hdmobHntQVM%2fA&pid=ImgRaw&r=0", description="Rich, fudgy brownies that satisfy your chocolate cravings.", product_group_id=4),

        # Pantry Staples
        Product(product_name="Canned Beans", price=2, image_url="https://th.bing.com/th/id/R.9f2e8d5686357bb42eda52ecb890b914?rik=MKlYKvJB2xTkHg&pid=ImgRaw&r=0", description="Convenient, versatile beans for soups, salads, and more.", product_group_id=5),
        Product(product_name="Pasta", price=3, image_url="https://th.bing.com/th/id/R.658b699164f07726d7fd994cdfe35525?rik=n%2fAoxRV8MO5r0g&pid=ImgRaw&r=0", description="A pantry essential for quick and delicious meals.", product_group_id=5),
        Product(product_name="Cooking Oil", price=5, image_url="https://th.bing.com/th/id/OIP._N07oIUR7vctMAs8zwivfQHaE8?rs=1&pid=ImgDetMain", description="High-quality cooking oil for all your culinary needs.", product_group_id=5),

        # Frozen Foods
        Product(product_name="Frozen Vegetables", price=4, image_url="https://th.bing.com/th/id/R.a6a5b7db6deadb16562728a355ac5059?rik=PUCEuWhfc9a8ew&pid=ImgRaw&r=0", description="Fresh and nutritious vegetables, ready to cook from frozen.", product_group_id=6),
        Product(product_name="Frozen Fish", price=8, image_url="https://timurikan.com.my/wp-content/uploads/2018/08/indian-mackerel.jpg", product_group_id=6),
        Product(product_name="Frozen Burgers", price=7, image_url="https://th.bing.com/th/id/OIP.UBtYOLcGF2VwtQM8Do9deQAAAA?rs=1&pid=ImgDetMain", description="Juicy, pre-made burgers, ready to grill and enjoy.", product_group_id=6),
    ]

    # Add products to the session
    for product in products:
        db.session.add(product)

    # Commit products to the database
    db.session.commit()

print("Database seeded successfully!")
