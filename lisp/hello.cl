;;;; 实用common lisp

(defvar *db* nil)

(defun hello-world ()
  "Now everything begin"
  (format t "Hello, World!"))

(defun add-record (cd)
  "Add CD record to db"
  (push cd *db*))

(defun dump-db ()
  "Output db"
  (dolist (cd *db*)
    (if (not (equal cd nil))
      (format t "~{~a: ~10t~a~%~}~%" cd))))

(defun load-db (filename)
  (with-open-file (in filename)
    (with-standard-io-syntax
      (setf *db* (read in)))))

(defun make-cd (title artist rating ripped)
  "Create CD record"
  (list :title title :artist artist :rating rating :ripped ripped))

(defun save-db (filename)
  "Save db"
  (with-open-file (out filename
                    :direction :output
                    :if-exists :supersede)
    (with-standard-io-syntax
      (print *db* out))))
