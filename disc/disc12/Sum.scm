(define (sum lst)
  (define (sum-helper l result)
    (if (null? l) result
	(sum-helper (cdr l) (+ result (car l)))))
  (sum-helper lst 0)
)

(expect (sum '(1 2 3)) 6)
(expect (sum '(10 -3 4)) 11)
