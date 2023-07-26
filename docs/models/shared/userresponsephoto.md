# UserResponsePhoto

A map of the user’s profile photo in various sizes, or null if no photo is set. Sizes provided are 21, 27, 36, 60, 128, and 1024. All images are in PNG format, except for 1024 (which is in JPEG format).


## Fields

| Field              | Type               | Required           | Description        |
| ------------------ | ------------------ | ------------------ | ------------------ |
| `image_1024x1024`  | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `image_128x128`    | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `image_21x21`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `image_27x27`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `image_36x36`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |
| `image_60x60`      | *Optional[str]*    | :heavy_minus_sign: | N/A                |