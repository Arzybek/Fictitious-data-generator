import statistics as stats

needed = {0, 2, 3, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 27, 28, 30, 33, 36, 37, 38, 40, 43, 44,
          47, 49, 52, 54, 55, 56, 57, 58, 61, 62, 63, 64, 67, 70, 72, 73, 75, 77, 79, 80, 81, 83, 84, 86, 87, 88, 90,
          93, 96, 97, 98, 99, 100, 101, 103, 104, 105, 106, 107, 108, 109, 112, 113, 117, 118, 119, 121, 122, 126, 128,
          130, 131, 133, 136, 138, 140, 141, 142, 146, 147, 149, 150, 152, 154, 155, 157, 158, 159, 161, 165, 166, 167,
          170, 171, 172, 173, 174, 176, 177, 178, 180, 181, 187, 192, 194, 195, 196, 199, 200, 201, 204, 207, 208, 209,
          210, 212, 213, 214, 216, 219, 224, 225, 226, 231, 232, 233, 234, 235, 239, 244, 245}
mails = ["@gmail.com",
         "@yandex.ru",
         "@outlook.com",
         "@mail.com",
         "@inbox.com",
         "@yahoo.com",
         "@protonmail.com"]
avg_age = 0
dispersion = 5
