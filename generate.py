import re

level_scalars = {
    1: ["alpha", "a", "b", "c", "s", "d1", "d2", "x1", "y1"],
    2: ["alpha", "beta"],
    3: ["alpha", "beta"],
}

def is_scalar(name, cty, f):
    return name in level_scalars[f.level]

level1_single = """
pub fn srotg_(a: *mut c_float, b: *mut c_float, c: *mut c_float, s: *mut c_float);
pub fn srotmg_(d1: *mut c_float, d2: *mut c_float, x1: *mut c_float, y1: *const c_float,
               param: *mut c_float);
pub fn srot_(n: *const c_int, x: *mut c_float, incx: *const c_int, y: *mut c_float,
             incy: *const c_int, c: *const c_float, s: *const c_float);
pub fn srotm_(n: *const c_int, x: *mut c_float, incx: *const c_int, y: *mut c_float,
              incy: *const c_int, param: *const c_float);
pub fn sswap_(n: *const c_int, x: *mut c_float, incx: *const c_int, y: *mut c_float,
              incy: *const c_int);
pub fn sscal_(n: *const c_int, a: *const c_float, x: *mut c_float, incx: *const c_int);
pub fn scopy_(n: *const c_int, x: *const c_float, incx: *const c_int, y: *mut c_float,
              incy: *const c_int);
pub fn saxpy_(n: *const c_int, alpha: *const c_float, x: *const c_float, incx: *const c_int,
              y: *mut c_float, incy: *const c_int);
pub fn sdot_(n: *const c_int, x: *const c_float, incx: *const c_int, y: *const c_float,
             incy: *const c_int) -> c_float;
pub fn sdsdot_(n: *const c_int, sb: *const c_float, x: *const c_float, incx: *const c_int,
               y: *const c_float, incy: *const c_int) -> c_float;
pub fn snrm2_(n: *const c_int, x: *const c_float, incx: *const c_int) -> c_float;
pub fn scnrm2_(n: *const c_int, x: *const complex_float, incx: *const c_int) -> c_float;
pub fn sasum_(n: *const c_int, x: *const c_float, incx: *const c_int) -> c_float;
pub fn isamax_(n: *const c_int, x: *const c_float, incx: *const c_int) -> c_int;
"""

level1_double = """
pub fn drotg_(a: *mut c_double, b: *mut c_double, c: *mut c_double, s: *mut c_double);
pub fn drotmg_(d1: *mut c_double, d2: *mut c_double, x1: *mut c_double, y1: *const c_double,
               param: *mut c_double);
pub fn drot_(n: *const c_int, x: *mut c_double, incx: *const c_int, y: *mut c_double,
             incy: *const c_int, c: *const c_double, s: *const c_double);
pub fn drotm_(n: *const c_int, x: *mut c_double, incx: *const c_int, y: *mut c_double,
              incy: *const c_int, param: *const c_double);
pub fn dswap_(n: *const c_int, x: *mut c_double, incx: *const c_int, y: *mut c_double,
              incy: *const c_int);
pub fn dscal_(n: *const c_int, a: *const c_double, x: *mut c_double, incx: *const c_int);
pub fn dcopy_(n: *const c_int, x: *const c_double, incx: *const c_int, y: *mut c_double,
              incy: *const c_int);
pub fn daxpy_(n: *const c_int, alpha: *const c_double, x: *const c_double, incx: *const c_int,
              y: *mut c_double, incy: *const c_int);
pub fn ddot_(n: *const c_int, x: *const c_double, incx: *const c_int, y: *const c_double,
             incy: *const c_int) -> c_double;
pub fn dsdot_(n: *const c_int, x: *const c_float, incx: *const c_int, y: *const c_float,
              incy: *const c_int) -> c_double;
pub fn dnrm2_(n: *const c_int, x: *const c_double, incx: *const c_int) -> c_double;
pub fn dznrm2_(n: *const c_int, x: *const complex_double, incx: *const c_int) -> c_double;
pub fn dasum_(n: *const c_int, x: *const c_double, incx: *const c_int) -> c_double;
pub fn idamax_(n: *const c_int, x: *const c_double, incx: *const c_int) -> c_int;
"""

level1_complex = """
pub fn crotg_(a: *mut complex_float, b: *const complex_float, c: *mut c_float,
              s: *mut complex_float);
pub fn csrot_(n: *const c_int, x: *mut complex_float, incx: *const c_int,
              y: *mut complex_float, incy: *const c_int, c: *const c_float, s: *const c_float);
pub fn cswap_(n: *const c_int, x: *mut complex_float, incx: *const c_int,
              y: *mut complex_float, incy: *const c_int);
pub fn cscal_(n: *const c_int, a: *const complex_float, x: *mut complex_float,
              incx: *const c_int);
pub fn csscal_(n: *const c_int, a: *const c_float, x: *mut complex_float, incx: *const c_int);
pub fn ccopy_(n: *const c_int, x: *const complex_float, incx: *const c_int,
              y: *mut complex_float, incy: *const c_int);
pub fn caxpy_(n: *const c_int, alpha: *const complex_float, x: *const complex_float,
              incx: *const c_int, y: *mut complex_float, incy: *const c_int);
pub fn cdotu_(pres: *mut complex_float, n: *const c_int, x: *const complex_float,
              incx: *const c_int, y: *const complex_float, incy: *const c_int);
pub fn cdotc_(pres: *mut complex_float, n: *const c_int, x: *const complex_float,
              incx: *const c_int, y: *const complex_float, incy: *const c_int);
pub fn scasum_(n: *const c_int, x: *const complex_float, incx: *const c_int) -> c_float;
pub fn icamax_(n: *const c_int, x: *const complex_float, incx: *const c_int) -> c_int;
"""

level1_double_complex = """
pub fn zrotg_(a: *mut complex_double, b: *const complex_double, c: *mut c_double,
              s: *mut complex_double);
pub fn zdrot_(n: *const c_int, x: *mut complex_double, incx: *const c_int,
              y: *mut complex_double, incy: *const c_int, c: *const c_double,
              s: *const c_double);
pub fn zswap_(n: *const c_int, x: *mut complex_double, incx: *const c_int,
              y: *mut complex_double, incy: *const c_int);
pub fn zscal_(n: *const c_int, a: *const complex_double, x: *mut complex_double,
              incx: *const c_int);
pub fn zdscal_(n: *const c_int, a: *const c_double, x: *mut complex_double,
               incx: *const c_int);
pub fn zcopy_(n: *const c_int, x: *const complex_double, incx: *const c_int,
              y: *mut complex_double, incy: *const c_int);
pub fn zaxpy_(n: *const c_int, alpha: *const complex_double, x: *const complex_double,
             incx: *const c_int, y: *mut complex_double, incy: *const c_int);
pub fn zdotu_(pres: *mut complex_double, n: *const c_int, x: *const complex_double,
              incx: *const c_int, y: *const complex_double, incy: *const c_int);
pub fn zdotc_(pres: *mut complex_double, n: *const c_int, x: *const complex_double,
              incx: *const c_int, y: *const complex_double, incy: *const c_int);
pub fn dzasum_(n: *const c_int, x: *const complex_double, incx: *const c_int) -> c_double;
pub fn izamax_(n: *const c_int, x: *const complex_double, incx: *const c_int) -> c_int;
"""

level2_single = """
pub fn sgemv_(trans: *const c_char, m: *const c_int, n: *const c_int, alpha: *const c_float,
              a: *const c_float, lda: *const c_int, x: *const c_float, incx: *const c_int,
              beta: *const c_float, y: *mut c_float, incy: *const c_int);
pub fn sgbmv_(trans: *const c_char, m: *const c_int, n: *const c_int, kl: *const c_int,
              ku: *const c_int, alpha: *const c_float, a: *const c_float, lda: *const c_int,
              x: *const c_float, incx: *const c_int, beta: *const c_float, y: *mut c_float,
              incy: *const c_int);
pub fn ssymv_(uplo: *const c_char, n: *const c_int, alpha: *const c_float, a: *const c_float,
              lda: *const c_int, x: *const c_float, incx: *const c_int, beta: *const c_float,
              y: *mut c_float, incy: *const c_int);
pub fn ssbmv_(uplo: *const c_char, n: *const c_int, k: *const c_int, alpha: *const c_float,
              a: *const c_float, lda: *const c_int, x: *const c_float, incx: *const c_int,
              beta: *const c_float, y: *mut c_float, incy: *const c_int);
pub fn sspmv_(uplo: *const c_char, n: *const c_int, alpha: *const c_float, ap: *const c_float,
              x: *const c_float, incx: *const c_int, beta: *const c_float, y: *mut c_float,
              incy: *const c_int);
pub fn strmv_(uplo: *const c_char, transa: *const c_char, diag: *const c_char, n: *const c_int,
              a: *const c_float, lda: *const c_int, b: *mut c_float, incx: *const c_int);
pub fn stbmv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              k: *const c_int, a: *const c_float, lda: *const c_int, x: *mut c_float,
              incx: *const c_int);
pub fn stpmv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              ap: *const c_float, x: *mut c_float, incx: *const c_int);
pub fn strsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              a: *const c_float, lda: *const c_int, x: *mut c_float, incx: *const c_int);
pub fn stbsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              k: *const c_int, a: *const c_float, lda: *const c_int, x: *mut c_float,
              incx: *const c_int);
pub fn stpsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              ap: *const c_float, x: *mut c_float, incx: *const c_int);
pub fn sger_(m: *const c_int, n: *const c_int, alpha: *const c_float, x: *const c_float,
             incx: *const c_int, y: *const c_float, incy: *const c_int, a: *mut c_float,
             lda: *const c_int);
pub fn ssyr_(uplo: *const c_char, n: *const c_int, alpha: *const c_float, x: *const c_float,
             incx: *const c_int, a: *mut c_float, lda: *const c_int);
pub fn sspr_(uplo: *const c_char, n: *const c_int, alpha: *const c_float, x: *const c_float,
             incx: *const c_int, ap: *mut c_float);
pub fn ssyr2_(uplo: *const c_char, n: *const c_int, alpha: *const c_float, x: *const c_float,
              incx: *const c_int, y: *const c_float, incy: *const c_int, a: *mut c_float,
              lda: *const c_int);
pub fn sspr2_(uplo: *const c_char, n: *const c_int, alpha: *const c_float, x: *const c_float,
              incx: *const c_int, y: *const c_float, incy: *const c_int, ap: *mut c_float);
"""

level2_double = """
pub fn dgemv_(trans: *const c_char, m: *const c_int, n: *const c_int, alpha: *const c_double,
              a: *const c_double, lda: *const c_int, x: *const c_double, incx: *const c_int,
              beta: *const c_double, y: *mut c_double, incy: *const c_int);
pub fn dgbmv_(trans: *const c_char, m: *const c_int, n: *const c_int, kl: *const c_int,
              ku: *const c_int, alpha: *const c_double, a: *const c_double, lda: *const c_int,
              x: *const c_double, incx: *const c_int, beta: *const c_double, y: *mut c_double,
              incy: *const c_int);
pub fn dsymv_(uplo: *const c_char, n: *const c_int, alpha: *const c_double, a: *const c_double,
              lda: *const c_int, x: *const c_double, incx: *const c_int, beta: *const c_double,
              y: *mut c_double, incy: *const c_int);
pub fn dsbmv_(uplo: *const c_char, n: *const c_int, k: *const c_int, alpha: *const c_double,
              a: *const c_double, lda: *const c_int, x: *const c_double, incx: *const c_int,
              beta: *const c_double, y: *mut c_double, incy: *const c_int);
pub fn dspmv_(uplo: *const c_char, n: *const c_int, alpha: *const c_double, ap: *const c_double,
              x: *const c_double, incx: *const c_int, beta: *const c_double,
              y: *mut c_double, incy: *const c_int);
pub fn dtrmv_(uplo: *const c_char, transa: *const c_char, diag: *const c_char, n: *const c_int,
              a: *const c_double, lda: *const c_int, b: *mut c_double, incx: *const c_int);
pub fn dtbmv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              k: *const c_int, a: *const c_double, lda: *const c_int, x: *mut c_double,
              incx: *const c_int);
pub fn dtpmv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              ap: *const c_double, x: *mut c_double, incx: *const c_int);
pub fn dtrsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              a: *const c_double, lda: *const c_int, x: *mut c_double, incx: *const c_int);
pub fn dtbsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              k: *const c_int, a: *const c_double, lda: *const c_int, x: *mut c_double,
              incx: *const c_int);
pub fn dtpsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              ap: *const c_double, x: *mut c_double, incx: *const c_int);
pub fn dger_(m: *const c_int, n: *const c_int, alpha: *const c_double, x: *const c_double,
             incx: *const c_int, y: *const c_double, incy: *const c_int, a: *mut c_double,
             lda: *const c_int);
pub fn dsyr_(uplo: *const c_char, n: *const c_int, alpha: *const c_double, x: *const c_double,
             incx: *const c_int, a: *mut c_double, lda: *const c_int);
pub fn dspr_(uplo: *const c_char, n: *const c_int, alpha: *const c_double, x: *const c_double,
             incx: *const c_int, ap: *mut c_double);
pub fn dsyr2_(uplo: *const c_char, n: *const c_int, alpha: *const c_double, x: *const c_double,
              incx: *const c_int, y: *const c_double, incy: *const c_int, a: *mut c_double,
              lda: *const c_int);
pub fn dspr2_(uplo: *const c_char, n: *const c_int, alpha: *const c_double, x: *const c_double,
              incx: *const c_int, y: *const c_double, incy: *const c_int, ap: *mut c_double);
"""

level2_complex = """
pub fn cgemv_(trans: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const complex_float, a: *const complex_float, lda: *const c_int,
              x: *const complex_float, incx: *const c_int, beta: *const complex_float,
              y: *mut complex_float, incy: *const c_int);
pub fn cgbmv_(trans: *const c_char, m: *const c_int, n: *const c_int, kl: *const c_int,
              ku: *const c_int, alpha: *const complex_float, a: *const complex_float,
              lda: *const c_int, x: *const complex_float, incx: *const c_int,
              beta: *const complex_float, y: *mut complex_float, incy: *const c_int);
pub fn chemv_(uplo: *const c_char, n: *const c_int, alpha: *const complex_float,
              a: *const complex_float, lda: *const c_int, x: *const complex_float,
              incx: *const c_int, beta: *const complex_float, y: *mut complex_float,
              incy: *const c_int);
pub fn chbmv_(uplo: *const c_char, n: *const c_int, k: *const c_int,
              alpha: *const complex_float, a: *const complex_float, lda: *const c_int,
              x: *const complex_float, incx: *const c_int, beta: *const complex_float,
              y: *mut complex_float, incy: *const c_int);
pub fn chpmv_(uplo: *const c_char, n: *const c_int, alpha: *const complex_float,
              ap: *const complex_float, x: *const complex_float, incx: *const c_int,
              beta: *const complex_float, y: *mut complex_float, incy: *const c_int);
pub fn ctrmv_(uplo: *const c_char, transa: *const c_char, diag: *const c_char, n: *const c_int,
              a: *const complex_float, lda: *const c_int, b: *mut complex_float,
              incx: *const c_int);
pub fn ctbmv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              k: *const c_int, a: *const complex_float, lda: *const c_int,
              x: *mut complex_float, incx: *const c_int);
pub fn ctpmv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              ap: *const complex_float, x: *mut complex_float, incx: *const c_int);
pub fn ctrsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              a: *const complex_float, lda: *const c_int, x: *mut complex_float,
              incx: *const c_int);
pub fn ctbsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              k: *const c_int, a: *const complex_float, lda: *const c_int,
              x: *mut complex_float, incx: *const c_int);
pub fn ctpsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              ap: *const complex_float, x: *mut complex_float, incx: *const c_int);
pub fn cgeru_(m: *const c_int, n: *const c_int, alpha: *const complex_float,
              x: *const complex_float, incx: *const c_int, y: *const complex_float,
              incy: *const c_int, a: *mut complex_float, lda: *const c_int);
pub fn cgerc_(m: *const c_int, n: *const c_int, alpha: *const complex_float,
              x: *const complex_float, incx: *const c_int, y: *const complex_float,
              incy: *const c_int, a: *mut complex_float, lda: *const c_int);
pub fn cher_(uplo: *const c_char, n: *const c_int, alpha: *const c_float,
             x: *const complex_float, incx: *const c_int, a: *mut complex_float,
             lda: *const c_int);
pub fn chpr_(uplo: *const c_char, n: *const c_int, alpha: *const c_float,
             x: *const complex_float, incx: *const c_int, ap: *mut complex_float);
pub fn chpr2_(uplo: *const c_char, n: *const c_int, alpha: *const complex_float,
              x: *const complex_float, incx: *const c_int, y: *const complex_float,
              incy: *const c_int, ap: *mut complex_float);
pub fn cher2_(uplo: *const c_char, n: *const c_int, alpha: *const complex_float, x: *const
              complex_float, incx: *const c_int, y: *const complex_float, incy: *const c_int,
              a: *mut complex_float, lda: *const c_int);
"""

level2_double_complex = """
pub fn zgemv_(trans: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const complex_double, a: *const complex_double, lda: *const c_int,
              x: *const complex_double, incx: *const c_int, beta: *const complex_double,
              y: *mut complex_double, incy: *const c_int);
pub fn zgbmv_(trans: *const c_char, m: *const c_int, n: *const c_int, kl: *const c_int,
              ku: *const c_int, alpha: *const complex_double, a: *const complex_double,
              lda: *const c_int, x: *const complex_double, incx: *const c_int,
              beta: *const complex_double, y: *mut complex_double, incy: *const c_int);
pub fn zhemv_(uplo: *const c_char, n: *const c_int, alpha: *const complex_double,
              a: *const complex_double, lda: *const c_int, x: *const complex_double,
              incx: *const c_int, beta: *const complex_double, y: *mut complex_double,
              incy: *const c_int);
pub fn zhbmv_(uplo: *const c_char, n: *const c_int, k: *const c_int,
              alpha: *const complex_double, a: *const complex_double, lda: *const c_int,
              x: *const complex_double, incx: *const c_int, beta: *const complex_double,
              y: *mut complex_double, incy: *const c_int);
pub fn zhpmv_(uplo: *const c_char, n: *const c_int, alpha: *const complex_double,
              ap: *const complex_double, x: *const complex_double, incx: *const c_int,
              beta: *const complex_double, y: *mut complex_double, incy: *const c_int);
pub fn ztrmv_(uplo: *const c_char, transa: *const c_char, diag: *const c_char, n: *const c_int,
              a: *const complex_double, lda: *const c_int, b: *mut complex_double,
              incx: *const c_int);
pub fn ztbmv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              k: *const c_int,
              a: *const complex_double, lda: *const c_int, x: *mut complex_double,
              incx: *const c_int);
pub fn ztpmv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              ap: *const complex_double, x: *mut complex_double, incx: *const c_int);
pub fn ztrsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              a: *const complex_double, lda: *const c_int, x: *mut complex_double,
              incx: *const c_int);
pub fn ztbsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              k: *const c_int, a: *const complex_double, lda: *const c_int,
              x: *mut complex_double, incx: *const c_int);
pub fn ztpsv_(uplo: *const c_char, trans: *const c_char, diag: *const c_char, n: *const c_int,
              ap: *const complex_double, x: *mut complex_double, incx: *const c_int);
pub fn zgeru_(m: *const c_int, n: *const c_int, alpha: *const complex_double,
              x: *const complex_double, incx: *const c_int, y: *const complex_double,
              incy: *const c_int, a: *mut complex_double, lda: *const c_int);
pub fn zgerc_(m: *const c_int, n: *const c_int, alpha: *const complex_double,
              x: *const complex_double, incx: *const c_int, y: *const complex_double,
              incy: *const c_int, a: *mut complex_double, lda: *const c_int);
pub fn zher_(uplo: *const c_char, n: *const c_int, alpha: *const c_double,
             x: *const complex_double, incx: *const c_int, a: *mut complex_double,
             lda: *const c_int);
pub fn zhpr_(uplo: *const c_char, n: *const c_int, alpha: *const c_double,
             x: *const complex_double, incx: *const c_int, ap: *mut complex_double);
pub fn zher2_(uplo: *const c_char, n: *const c_int, alpha: *const complex_double,
              x: *const complex_double, incx: *const c_int, y: *const complex_double,
              incy: *const c_int, a: *mut complex_double, lda: *const c_int);
pub fn zhpr2_(uplo: *const c_char, n: *const c_int, alpha: *const complex_double,
              x: *const complex_double, incx: *const c_int, y: *const complex_double,
              incy: *const c_int, ap: *mut complex_double);
"""

level3_single = """
pub fn sgemm_(transa: *const c_char, transb: *const c_char, m: *const c_int, n: *const c_int,
              k: *const c_int, alpha: *const c_float, a: *const c_float, lda: *const c_int,
              b: *const c_float, ldb: *const c_int,
              beta: *const c_float, c: *mut c_float, ldc: *const c_int);
pub fn ssymm_(side: *const c_char, uplo: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const c_float, a: *const c_float, lda: *const c_int, b: *const c_float,
              ldb: *const c_int, beta: *const c_float, c: *mut c_float, ldc: *const c_int);
pub fn ssyrk_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
              alpha: *const c_float, a: *const c_float, lda: *const c_int, beta: *const c_float,
              c: *mut c_float, ldc: *const c_int);
pub fn ssyr2k_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
               alpha: *const c_float, a: *const c_float, lda: *const c_int, b: *const c_float,
               ldb: *const c_int, beta: *const c_float, c: *mut c_float, ldc: *const c_int);
pub fn strmm_(side: *const c_char, uplo: *const c_char, transa: *const c_char,
              diag: *const c_char, m: *const c_int, n: *const c_int, alpha: *const c_float,
              a: *const c_float, lda: *const c_int, b: *mut c_float, ldb: *const c_int);
pub fn strsm_(side: *const c_char, uplo: *const c_char, transa: *const c_char,
              diag: *const c_char, m: *const c_int, n: *const c_int, alpha: *const c_float,
              a: *const c_float, lda: *const c_int, b: *mut c_float, ldb: *const c_int);
"""

level3_double = """
pub fn dgemm_(transa: *const c_char, transb: *const c_char, m: *const c_int, n: *const c_int,
              k: *const c_int, alpha: *const c_double, a: *const c_double, lda: *const c_int,
              b: *const c_double, ldb: *const c_int, beta: *const c_double, c: *mut c_double,
              ldc: *const c_int);
pub fn dsymm_(side: *const c_char, uplo: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const c_double, a: *const c_double, lda: *const c_int,
              b: *const c_double, ldb: *const c_int, beta: *const c_double, c: *mut c_double,
              ldc: *const c_int);
pub fn dsyrk_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
              alpha: *const c_double, a: *const c_double, lda: *const c_int,
              beta: *const c_double, c: *mut c_double, ldc: *const c_int);
pub fn dsyr2k_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
               alpha: *const c_double, a: *const c_double, lda: *const c_int,
               b: *const c_double, ldb: *const c_int, beta: *const c_double, c: *mut c_double,
               ldc: *const c_int);
pub fn dtrmm_(side: *const c_char, uplo: *const c_char, transa: *const c_char,
              diag: *const c_char, m: *const c_int, n: *const c_int, alpha: *const c_double,
              a: *const c_double, lda: *const c_int, b: *mut c_double, ldb: *const c_int);
pub fn dtrsm_(side: *const c_char, uplo: *const c_char, transa: *const c_char,
              diag: *const c_char, m: *const c_int, n: *const c_int, alpha: *const c_double,
              a: *const c_double, lda: *const c_int, b: *mut c_double, ldb: *const c_int);
"""

level3_complex = """
pub fn cgemm_(transa: *const c_char, transb: *const c_char, m: *const c_int, n: *const c_int,
              k: *const c_int, alpha: *const complex_float, a: *const complex_float,
              lda: *const c_int, b: *const complex_float, ldb: *const c_int,
              beta: *const complex_float, c: *mut complex_float, ldc: *const c_int);
pub fn csymm_(side: *const c_char, uplo: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const complex_float, a: *const complex_float, lda: *const c_int,
              b: *const complex_float, ldb: *const c_int, beta: *const complex_float,
              c: *mut complex_float, ldc: *const c_int);
pub fn chemm_(side: *const c_char, uplo: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const complex_float, a: *const complex_float, lda: *const c_int,
              b: *const complex_float, ldb: *const c_int, beta: *const complex_float,
              c: *mut complex_float, ldc: *const c_int);
pub fn csyrk_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
              alpha: *const complex_float, a: *const complex_float, lda: *const c_int,
              beta: *const complex_float, c: *mut complex_float, ldc: *const c_int);
pub fn cherk_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
              alpha: *const c_float, a: *const complex_float, lda: *const c_int,
              beta: *const c_float, c: *mut complex_float, ldc: *const c_int);
pub fn csyr2k_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
               alpha: *const complex_float, a: *const complex_float, lda: *const c_int,
               b: *const complex_float, ldb: *const c_int, beta: *const complex_float,
               c: *mut complex_float, ldc: *const c_int);
pub fn cher2k_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
               alpha: *const complex_float, a: *const complex_float, lda: *const c_int,
               b: *const complex_float, ldb: *const c_int, beta: *const c_float,
               c: *mut complex_float, ldc: *const c_int);
pub fn ctrmm_(side: *const c_char, uplo: *const c_char, transa: *const c_char,
              diag: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const complex_float, a: *const complex_float, lda: *const c_int,
              b: *mut complex_float, ldb: *const c_int);
pub fn ctrsm_(side: *const c_char, uplo: *const c_char, transa: *const c_char,
              diag: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const complex_float, a: *const complex_float, lda: *const c_int,
              b: *mut complex_float, ldb: *const c_int);
"""

level3_double_complex = """
pub fn zgemm_(transa: *const c_char, transb: *const c_char, m: *const c_int, n: *const c_int,
              k: *const c_int, alpha: *const complex_double, a: *const complex_double,
              lda: *const c_int, b: *const complex_double, ldb: *const c_int,
              beta: *const complex_double, c: *mut complex_double, ldc: *const c_int);
pub fn zsymm_(side: *const c_char, uplo: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const complex_double, a: *const complex_double, lda: *const c_int,
              b: *const complex_double, ldb: *const c_int, beta: *const complex_double,
              c: *mut complex_double, ldc: *const c_int);
pub fn zhemm_(side: *const c_char, uplo: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const complex_double, a: *const complex_double, lda: *const c_int,
              b: *const complex_double, ldb: *const c_int, beta: *const complex_double,
              c: *mut complex_double, ldc: *const c_int);
pub fn zsyrk_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
              alpha: *const complex_double, a: *const complex_double, lda: *const c_int,
              beta: *const complex_double, c: *mut complex_double, ldc: *const c_int);
pub fn zherk_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
              alpha: *const c_double, a: *const complex_double, lda: *const c_int,
              beta: *const c_double, c: *mut complex_double, ldc: *const c_int);
pub fn zsyr2k_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
               alpha: *const complex_double, a: *const complex_double, lda: *const c_int,
               b: *const complex_double, ldb: *const c_int, beta: *const complex_double,
               c: *mut complex_double, ldc: *const c_int);
pub fn zher2k_(uplo: *const c_char, trans: *const c_char, n: *const c_int, k: *const c_int,
               alpha: *const complex_double, a: *const complex_double, lda: *const c_int,
               b: *const complex_double, ldb: *const c_int, beta: *const c_double,
               c: *mut complex_double, ldc: *const c_int);
pub fn ztrmm_(side: *const c_char, uplo: *const c_char, transa: *const c_char,
              diag: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const complex_double, a: *const complex_double, lda: *const c_int,
              b: *mut complex_double, ldb: *const c_int);
pub fn ztrsm_(side: *const c_char, uplo: *const c_char, transa: *const c_char,
              diag: *const c_char, m: *const c_int, n: *const c_int,
              alpha: *const complex_double, a: *const complex_double, lda: *const c_int,
              b: *mut complex_double, ldb: *const c_int);
"""

name_re = re.compile("pub fn (\w+)_")
argument_re = re.compile("(\w+): ([^,]*)(,|\))")
return_re = re.compile("(?:\s*->\s*([^;]+))?");

def pull_name(s):
    m = name_re.match(s)
    assert(m is not None)
    return m.group(1), s[m.end(1)+1:]

def pull_argument(s):
    m = argument_re.match(s)
    if m is None:
        return None, None, s

    return m.group(1), m.group(2), s[m.end(3):]

def pull_return(s):
    m = return_re.match(s)
    if m is None:
        return None, s

    return m.group(1), s[m.end(1):]

def chew(s, c):
    assert s[0] == c
    return s[1:]

class Func(object):
    def __init__(self, level, name, args, ret):
        self.level = level
        self.name = name
        self.args = args
        self.ret = ret

    @staticmethod
    def parse(level, line):
        name, line = pull_name(line)
        if name is None:
            return None

        line = chew(line, '(')
        args = []
        while True:
            arg, aty, line = pull_argument(line)
            if arg is None:
                break
            args.append((arg, aty))
            line = line.strip()

        ret, line = pull_return(line)

        return Func(level, name, args, ret)

def is_const(name, cty):
    return "*const" in cty

def is_letter(name, cty):
    return "c_char" in cty

def is_natural(name, cty):
    return "c_int" in cty and (
        name in ["m", "n", "k", "kl", "ku"] or
        name.startswith("ld") or
        name.startswith("inc")
    )

def is_mut(name, cty):
    return "*mut" in cty

def translate_argument(name, cty, f):
    if is_natural(name, cty):
        assert(is_const(name, cty))
        return "usize"

    elif is_letter(name, cty):
        assert(is_const(name, cty))
        return "u8"

    elif is_const(name, cty):
        base = translate_type_base(cty)
        if is_scalar(name, cty, f):
            return base
        else:
            return "&[{}]".format(base)
    elif is_mut(name, cty):
        base = translate_type_base(cty)
        if is_scalar(name, cty, f):
            return "&mut {}".format(base)
        else:
            return "&mut [{}]".format(base)

    assert False, "cannot translate `{}: {}`".format(name, cty)

def translate_type_base(cty):
    if "complex_double" in cty:
        return "c64"
    elif "complex_float" in cty:
        return "c32"
    elif "double" in cty:
        return "f64"
    elif "float" in cty:
        return "f32"

    assert False, "cannot translate `{}`".format(cty)

def translate_body_argument(name, rty):
    if rty == "u8":
        return "&({} as c_char)".format(name)

    elif rty == "usize":
        return "&({} as c_int)".format(name)

    elif rty.startswith("f"):
        return "&{}".format(name)
    elif rty.startswith("&mut f"):
        return "{}".format(name)
    elif rty.startswith("&[f"):
        return "{}.as_ptr()".format(name)
    elif rty.startswith("&mut [f"):
        return "{}.as_mut_ptr()".format(name)

    elif rty.startswith("c"):
        return "&{} as *const _ as *const _".format(name)
    elif rty.startswith("&mut c"):
        return "{} as *mut _ as *mut _".format(name)
    elif rty.startswith("&[c"):
        return "{}.as_ptr() as *const _".format(name)
    elif rty.startswith("&mut [c"):
        return "{}.as_mut_ptr() as *mut _".format(name)

    assert False, "cannot translate `{}: {}`".format(name, rty)

def translate_return_type(cty):
    if cty == "c_int":
        return "isize"
    elif cty == "c_float":
        return "f32"
    elif cty == "c_double":
        return "f64"

    assert False, "cannot translate `{}`".format(cty)

def format_header(f):
    args = format_header_arguments(f)
    ret = "" if f.ret is None else " -> {}".format(translate_return_type(f.ret))
    header = "pub fn {}({}){} {{".format(f.name, args, ret)

    s = []
    indent = 7 + len(f.name) + 1
    while True:
        if len(header) <= 99:
            s.append(header)
            break
        k = 98 - header[98::-1].index(',')
        if k < 0:
            s.append(header)
            break
        s.append(header[:k+1])
        header = "{}{}".format(" " * indent, header[k+2:])

    if len(s) > 1:
        s.append("")

    return "\n".join(s)

def format_body(f):
    a = format_body_arguments(f)
    if f.ret is None:
        a = "{})".format(a)
    if f.ret is not None:
        a = "{}) as {}".format(a, translate_return_type(f.ret))

    s = []
    s.append(" " * 4)
    s.append("unsafe {\n")
    s.append(" " * 8)
    s.append("ffi::{}_(".format(f.name))

    a = "".join(a)
    indent = 8 + 5 + len(f.name) + 2
    while len(a) > 0:
        if len(a) + indent > 99:
            k = a.find(",")
            if k < 0 or k > 98:
                assert False, "cannot format `{}`".format(f.name)
            while True:
                l = a.find(",", k + 1)
                if l < 0 or l + indent > 98: break
                k = l
            s.append(a[0:k+1])
            s.append("\n")
            s.append(" " * indent)
            a = a[k+2:]
        else:
            s.append(a)
            a = ""

    s.append("\n")
    s.append(" " * 4)
    s.append("}")

    return "".join(s)

def format_header_arguments(f):
    s = []
    for arg in f.args:
        s.append("{}: {}".format(arg[0], translate_argument(*arg, f=f)))
    return ", ".join(s)

def format_body_arguments(f):
    s = []
    for arg in f.args:
        rty = translate_argument(*arg, f=f)
        s.append(translate_body_argument(arg[0], rty))
    return ", ".join(s)

def prepare(level, code):
    lines = re.sub(r'\s+', ' ', "".join(code.split('\n'))).strip().split(';')
    lines = filter(lambda line: not re.match(r'^\s*$', line), lines)
    return [Func.parse(level, line) for line in lines]

def do(funcs):
    for f in funcs:
        print("#[inline]")
        print(format_header(f))
        print(format_body(f))
        print("}\n")

do(prepare(1, level1_single))
do(prepare(1, level1_double))
do(prepare(1, level1_complex))
do(prepare(1, level1_double_complex))

do(prepare(2, level2_single))
do(prepare(2, level2_double))
do(prepare(2, level2_complex))
do(prepare(2, level2_double_complex))

do(prepare(3, level3_single))
do(prepare(3, level3_double))
do(prepare(3, level3_complex))
do(prepare(3, level3_double_complex))
