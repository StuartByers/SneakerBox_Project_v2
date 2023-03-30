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

sneaker_1 = Sneaker("Jordan 1", brand_2, 165, "https://cms-cdn.thesolesupplier.co.uk/2022/03/air-jordan-1-high-og-lost-found-dz5485-612_w1024_h1024_pad_.jpg.webp", False)
sneaker_repository.save(sneaker_1)

sneaker_2 = Sneaker("Dunk", brand_1, 100, "https://cms-cdn.thesolesupplier.co.uk/2020/05/nike-dunk-low-retro-black-white_w1024_h1024_pad_.jpg.webp", False)
sneaker_repository.save(sneaker_2)

sneaker_3 = Sneaker("350 v2", brand_4, 180, "https://cms-cdn.thesolesupplier.co.uk/2018/10/Yeezy-Boost-350-V2-Zebra-Restock_w1024_h1024_pad_.jpg.webp", False)
sneaker_repository.save(sneaker_3)

sneaker_4 = Sneaker("UltraBoost", brand_3, 140, "https://cms-cdn.thesolesupplier.co.uk/2020/12/adidas-ultra-boost-10-black-reflective_w1024_h1024_pad_.jpg.webp", False)
sneaker_repository.save(sneaker_4)

sneaker_5 = Sneaker("Jordan 3", brand_2, 190, "https://cms-cdn.thesolesupplier.co.uk/2022/05/air-jordan-3-white-cement-reimagined-dn3707-100-1_w1024_h1024_pad_.jpg.webp", False)
sneaker_repository.save(sneaker_5)

sneaker_6 = Sneaker("700", brand_4, 250, "https://cms-cdn.thesolesupplier.co.uk/2022/10/yeezy-boost-700-gs-wave-runner-fu9005_w1024_h1024_pad_.jpg.webp", False)
sneaker_repository.save(sneaker_6)
