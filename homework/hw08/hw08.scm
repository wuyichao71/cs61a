(define (my-filter pred s)
  (cond
   ((null? s) s)
   ((pred (car s)) (cons (car s) (my-filter pred (cdr s))))
   (else (my-filter pred (cdr s)))))

(define (interleave lst1 lst2) 'YOUR-CODE-HERE)

(define (accumulate joiner start n term)
  'YOUR-CODE-HERE)

(define (no-repeats lst) 'YOUR-CODE-HERE)
