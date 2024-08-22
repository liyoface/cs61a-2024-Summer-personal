(define (over-or-under num1 num2) 
    ; (cond ((< num1 num2) -1)
    ;       ((= num1 num2) 0)
    ;       (else 1))
    (if (< num1 num2) -1 (if (= num1 num2) 0 1))
    )

(define (make-adder num) 
    (lambda (inc) (+ num inc))
    ; (define (adder inc) (+ num inc))
    ; adder
    )

(define (composed f g) 
    (lambda (x) (f (g x)))
    )

(define (repeat f n)
    (if (< n 1)
        (lambda (x) x)
        (composed f (repeat f (- n 1)))
    ))

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
    (cond ((zero? a) b)
          ((zero? b) a)
          ((= (modulo (max a b) (min a b)) 0) (min a b))
          (else (gcd (min a b) (modulo (max a b) (min a b))))
        )
    )

(define (duplicate lst) 
    ; (print lst)
    (if (null? lst)
        lst
        (cons (car lst) 
              (cons (car lst)
                    (duplicate (cdr lst)))))
    )

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s) 
    (cond ((null? s) s)
        ((list? (car s))
        (cons (deep-map fn (car s)) 
              (deep-map fn (cdr s))))
        (else (cons (fn (car s))
              (deep-map fn (cdr s))))
        ))
