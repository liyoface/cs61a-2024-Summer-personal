(define (distance city-a city-b)
    (define dx (- (get-lon city-a) (get-lon city-b)))
    (define dy (- (get-lat city-a) (get-lat city-b)))
    (sqrt (+ (expt dx 2) (expt dy 2)))
)

(define (closer-city lat lon city-a city-b)
    (dis)
)
