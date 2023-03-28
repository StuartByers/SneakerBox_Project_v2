from models.sneaker import Sneaker
from models.brand import Brand
import repositories.sneaker_repository as sneaker_repository
import repositories.brand_repository as brand_repository

sneaker_repository.delete_all()
brand_repository.delete_all()

brand_1 = Brand("Nike")
brand_repository.save(brand_1)

brand_2 = Brand("Jordan Brand")
brand_repository.save(brand_2)

brand_3 = Brand("Adidas")
brand_repository.save(brand_3)

brand_4 = Brand("Yeezy")
brand_repository.save(brand_4)

sneaker_1 = Sneaker("Jordan 1", brand_2, 165, "https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/zzmfk3kwuw3ktkilxfnp/air-jordan-1-mid-shoes-MsflqZ.png", False)
sneaker_repository.save(sneaker_1)

sneaker_2 = Sneaker("Dunk", brand_1, 100, "https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/zzmfk3kwuw3ktkilxfnp/air-jordan-1-mid-shoes-MsflqZ.png", False)
sneaker_repository.save(sneaker_2)

sneaker_3 = Sneaker("350 v2", brand_4, 180, "https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/zzmfk3kwuw3ktkilxfnp/air-jordan-1-mid-shoes-MsflqZ.png", False)
sneaker_repository.save(sneaker_3)

sneaker_4 = Sneaker("UltraBoost", brand_3, 140, "https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/zzmfk3kwuw3ktkilxfnp/air-jordan-1-mid-shoes-MsflqZ.png", False)
sneaker_repository.save(sneaker_4)

sneaker_5 = Sneaker("Jordan 3", brand_2, 190, "https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/zzmfk3kwuw3ktkilxfnp/air-jordan-1-mid-shoes-MsflqZ.png", False)
sneaker_repository.save(sneaker_5)

sneaker_6 = Sneaker("700", brand_4, 250, "https://static.nike.com/a/images/t_PDP_864_v1/f_auto,b_rgb:f5f5f5/zzmfk3kwuw3ktkilxfnp/air-jordan-1-mid-shoes-MsflqZ.png", False)
sneaker_repository.save(sneaker_6)
