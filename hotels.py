
def awardTopKHotels(positiveKeywords, negativeKeywords, hotelIds, reviews, k):
    positive_Keywords = set(positiveKeywords.split(" "))
    negative_Keywords = set(negativeKeywords.split(" "))

    hotels_reviews = {}
    hotel_scores = {}

    for i in range(len(reviews)):
        reviews[i].replace(',', '')
        reviews[i].replace('.', '')
        review_splitted = reviews[i].split(" ")
        if hotelIds[i] in hotels_reviews:
            hotels_reviews[hotelIds[i]] += review_splitted
        else:
            hotels_reviews[hotelIds[i]] = [word for word in review_splitted]

    print(hotels_reviews)

    for item, val in hotels_reviews.items():
        score = 0
        for word in val:
            if word in positive_Keywords:
                score += 3
            elif word in negative_Keywords:
                score += 1

        hotel_scores[item] = score

    hotel_scores = {k: v for k, v in sorted(
        hotel_scores.items(), key=lambda item: item[1], reverse=True)}
    print(hotel_scores)
    return list(hotel_scores.keys())[:k]
