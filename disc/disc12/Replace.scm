(define (replace-helper e o n)
  (if (null? e) nil
      (if (equal? (car e) o) (cons n (replace-helper (cdr e) o n))
      (cons (car e) (replace-helper (cdr e) o n)))))
(define-macro (replace expr old new)
    (replace-helper expr old new))
