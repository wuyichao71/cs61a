(define (if-program condition if-true if-false)
  `(if ,condition ,if-true ,if-false)
)
(if-program '(= 0 0) '2 '3)
(eval (if-program '(= 0 0) '2 '3))
(if-program '(= 1 0) '(print 3) '(print 5))
(eval (if-program '(= 1 0) '(print 3) '(print 5)))
