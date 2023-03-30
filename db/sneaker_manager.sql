DROP TABLE IF EXISTS sneakers;
DROP TABLE IF EXISTS brands;

CREATE TABLE brands (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE sneakers (
  id SERIAL PRIMARY KEY,
  model VARCHAR(255),
  price INT,
  listed BOOLEAN,
  image_url VARCHAR(2048),
  brand_id INT NOT NULL REFERENCES brands(id)
);

INSERT INTO brands (name) VALUES ('Nike');

INSERT INTO brands (name) VALUES ('Adidas');

INSERT INTO brands (name) VALUES ('Jordan Brand');

INSERT INTO brands (name) VALUES ('Yeezy');

-- INSERT INTO sneakers (model, price, listed, image_url, brand_id) VALUES ("Jordan 1", 165, False, "https://cms-cdn.thesolesupplier.co.uk/2022/03/air-jordan-1-high-og-lost-found-dz5485-612_w1024_h1024_pad_.jpg.webp", 2);

-- INSERT INTO sneakers (model, price, listed, image_url, brand_id) VALUES ("Dunk", 100, False, "https://cms-cdn.thesolesupplier.co.uk/2020/05/nike-dunk-low-retro-black-white_w1024_h1024_pad_.jpg.webp", 1);

-- INSERT INTO sneakers (model, price, listed, image_url, brand_id) VALUES ("350 v2", 180, False, "https://cms-cdn.thesolesupplier.co.uk/2018/10/Yeezy-Boost-350-V2-Zebra-Restock_w1024_h1024_pad_.jpg.webp", 4);

-- INSERT INTO sneakers (model, price, listed, image_url, brand_id) VALUES ("UltraBoost", 140, False, "https://cms-cdn.thesolesupplier.co.uk/2020/12/adidas-ultra-boost-10-black-reflective_w1024_h1024_pad_.jpg.webp", 3);

-- INSERT INTO sneakers (model, price, listed, image_url, brand_id) VALUES ("Jordan 3", 190, False, "https://cms-cdn.thesolesupplier.co.uk/2022/05/air-jordan-3-white-cement-reimagined-dn3707-100-1_w1024_h1024_pad_.jpg.webp", 2);

-- INSERT INTO sneakers (model, price, listed, image_url, brand_id) VALUES ("700", 250, False, "https://cms-cdn.thesolesupplier.co.uk/2022/10/yeezy-boost-700-gs-wave-runner-fu9005_w1024_h1024_pad_.jpg.webp", 4);
