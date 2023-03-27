(define (reverse lst)
  (define (reverse-helper lst result)
    (if (null? lst) result
	(reverse-helper (cdr lst) (cons (car lst) result))))
  (reverse-helper lst nil)
)

(expect (reverse '(1 2 3)) (3 2 1))
(expect (reverse '(0 9 1 2)) (2 1 9 0))
