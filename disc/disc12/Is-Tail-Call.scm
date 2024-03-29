(define (question-a x)
  (if (= x 0) 0
      (+ x (question-a (- x 1)))))

(define (question-b x y)
  (if (= x 0) y
      (question-b (- x 1) (+ y x))))

(define (question-c x y)
  (if (> x y)
      (question-c (- y 1) x)
      (question-c (+ x 10) y)))

(define (question-d n)
  (if (question-d n)
      (question-d (- n 1))
      (question-d (+ n 10))))

(define (question-e n)
  (cond ((<= n 1) 1)
        ((question-e (- n 1)) (question-e (- n 2)))
        (else (begin (print 2) (question-e (- n 3))))))
