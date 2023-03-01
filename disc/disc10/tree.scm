(define (tree label children) (cons label children))
(define (label tr) (car tr))
(define (children tr) (cdr tr))
(define (is-leaf tr) (null? (children tr)))

(define (double tr)
  (tree (* 2 (label tr)) (map double (children tr))))

(define aTree (tree 6
		    (list (tree 3 (list (tree 1 nil)))
			  (tree 5 nil)
			  (tree 7 (list (tree 8 nil) (tree 9 nil))))))
(print aTree)
(double aTree)
