# Modul [03] - Trigonometri

**Nama:** Muhammad Gotzone Davu Quinn  
**NIM:** 1306625022

**Kelas:** Fisika C

---

## 1. Problem Statement
> Membuat Program untuk menghitung nilai sin dan cos dengan pendekatan deret Maclaurin

## 2. Mathematical Equation

### a. Deret Maclaurin untuk Sinus

Deret Maclaurin untuk fungsi sinus adalah:

$$
\sin x = \sum_{n=0}^{\infty} (-1)^n
\frac{x^{2n+1}}{(2n+1)!}
$$

Bentuk deretnya:

$$\sin x =x - \frac{x^3}{3!}+ \frac{x^5}{5!}- \frac{x^7}{7!}+ \cdots$$

### b. Deret Maclaurin untuk Cosinus

Deret Maclaurin untuk fungsi cosinus adalah:

$$
\cos x = \sum_{n=0}^{\infty} (-1)^n
\frac{x^{2n}}{(2n)!}
$$

Bentuk deretnya:

$$\cos x =1 - \frac{x^2}{2!}+ \frac{x^4}{4!}- \frac{x^6}{6!}+ \cdots$$

### c. Rumus Relative Error ($E_r$)

Relative Error digunakan untuk mengetahui seberapa besar perbedaan antara nilai eksak dan nilai hampiran.

$$
E_r =
\left|
\frac{x_{\text{true}} - x_{\text{approx}}}
{x_{\text{true}}}
\right|
\times 100\%
$$

Keterangan:

- $x_{\text{true}}$ : nilai eksak, misalnya dari fungsi `sin()` atau `cos()` bawaan.
- $x_{\text{approx}}$ : nilai hampiran yang diperoleh dari penjumlahan deret Maclaurin.
## 3. Algorithm
> Tuliskan langkah-langkah logika penyelesaian masalah secara sistematis sebelum diimplementasikan ke dalam kode Python (`main.py`).
