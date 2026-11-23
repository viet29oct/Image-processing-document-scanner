import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path



SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent

IMAGE_PATH = PROJECT_DIR / "source" / "otsu_thresholding.png"


# ==========================================================
# THUẬT TOÁN OTSU
# ==========================================================

def otsu_threshold(gray_img):
    # Ảnh xám có 256 mức:
    # 0 -> 255
    L = 256

    # Histogram
    # hist[i] = số pixel có mức xám i
    hist, _ = np.histogram(
        gray_img.ravel(),
        bins=L,
        range=(0, L)
    )

    # Tổng số pixel
    N = gray_img.size

    # Xác suất xuất hiện mỗi mức xám
    # p(i) = hist(i) / N
    p = hist / N

    # BIẾN DÙNG ĐỂ TÌM NGƯỠNG TỐI ƯU
    max_variance = -1.0

    best_threshold = 0

    # Lưu phương sai của từng ngưỡng
    # để vẽ biểu đồ
    variance_list = np.zeros(L)
    for t in range(L - 1):
        # w: tỉ lệ pixel của mỗi lớp
        # mu: mức xám trung bình của mỗi lớp
        # sigma_b_squared: độ tách biệt giữa hai lớp
        w1 = np.sum(
            p[:t + 1]
        )
        w2 = np.sum(
            p[t + 1:]
        )
        # Nếu một lớp không có pixel
        if w1 == 0 or w2 == 0:
            continue
        gray_levels_c1 = np.arange(
            0,
            t + 1
        )
        gray_levels_c2 = np.arange(
            t + 1,
            L
        )
        mu1 = (
            np.sum(
                gray_levels_c1
                * p[:t + 1]
            )
            / w1
        )
        mu2 = (
            np.sum(
                gray_levels_c2
                * p[t + 1:]
            )
            / w2
        )
        sigma_b_squared = (
            w1
            * w2
            * (mu1 - mu2) ** 2
        )
        # Lưu để lát nữa vẽ biểu đồ
        variance_list[t] = sigma_b_squared

        if sigma_b_squared > max_variance:

            max_variance = sigma_b_squared

            best_threshold = t

    return (
        best_threshold,
        hist,
        variance_list,
        max_variance
    )


# ==========================================================
# 5 PHƯƠNG PHÁP SIMPLE THRESHOLDING
# ==========================================================

def apply_threshold_methods(gray_img, threshold):

    maxval = 255


    # ======================================================
    # 1. BINARY
    #
    # src > T  -> 255
    # src <= T -> 0
    # ======================================================

    binary = np.where(
        gray_img > threshold,
        maxval,
        0
    ).astype(np.uint8)


    # ======================================================
    # 2. BINARY INVERTED
    #
    # src > T  -> 0
    # src <= T -> 255
    # ======================================================

    binary_inv = np.where(
        gray_img > threshold,
        0,
        maxval
    ).astype(np.uint8)


    # ======================================================
    # 3. TRUNCATED
    #
    # src > T  -> T
    # src <= T -> giữ nguyên
    # ======================================================

    trunc = np.where(
        gray_img > threshold,
        threshold,
        gray_img
    ).astype(np.uint8)


    # ======================================================
    # 4. TO ZERO
    #
    # src > T  -> giữ nguyên
    # src <= T -> 0
    # ======================================================

    tozero = np.where(
        gray_img > threshold,
        gray_img,
        0
    ).astype(np.uint8)


    # ======================================================
    # 5. TO ZERO INVERTED
    #
    # src > T  -> 0
    # src <= T -> giữ nguyên
    # ======================================================

    tozero_inv = np.where(
        gray_img > threshold,
        0,
        gray_img
    ).astype(np.uint8)


    return (
        binary,
        binary_inv,
        trunc,
        tozero,
        tozero_inv
    )




if __name__ == "__main__":

    print("Đường dẫn ảnh:")
    print(IMAGE_PATH)

    img_bgr = cv2.imread(
        str(IMAGE_PATH)
    )


    if img_bgr is None:

        print("\nKhông tìm thấy ảnh!")

        print(
            "Kiểm tra lại file:"
        )
        print(IMAGE_PATH)
        exit()

    img_rgb = cv2.cvtColor(
        img_bgr,
        cv2.COLOR_BGR2RGB
    )

    img_gray = cv2.cvtColor(
        img_bgr,
        cv2.COLOR_BGR2GRAY
    )
    # ======================================================
    # CHẠY OTSU TỰ VIẾT
    # ======================================================
    (
        best_threshold,
        histogram,
        variance_list,
        max_variance
    ) = otsu_threshold(img_gray)


    print("\n========= KẾT QUẢ OTSU =========")

    print(
        f"Ngưỡng tối ưu t* tự code: "
        f"{best_threshold}"
    )

    print(
        f"Phương sai cực đại: "
        f"{max_variance:.4f}"
    )

    opencv_threshold, _ = cv2.threshold(
        img_gray,
        0,
        255,
        cv2.THRESH_BINARY
        + cv2.THRESH_OTSU
    )


    print(
        f"Ngưỡng Otsu OpenCV: "
        f"{int(opencv_threshold)}"
    )


    if best_threshold == int(opencv_threshold):

        print(
            "=> Kết quả tự code trùng với OpenCV."
        )

    else:

        print(
            "=> Kết quả có sự khác nhau."
        )

    (
        dst_binary,
        dst_binary_inv,
        dst_trunc,
        dst_tozero,
        dst_tozero_inv
    ) = apply_threshold_methods(
        img_gray,
        best_threshold
    )


    # ======================================================
    # PHẦN 4 - HIỂN THỊ KẾT QUẢ
    # ======================================================

    plt.figure(
        figsize=(18, 10)
    )


    # ======================================================
    # 1. ẢNH GỐC
    # ======================================================

    plt.subplot(
        2,
        4,
        1
    )

    plt.imshow(
        img_rgb
    )

    plt.title(
        "Ảnh gốc màu"
    )

    plt.axis(
        "off"
    )


    # ======================================================
    # 2. ẢNH GRAYSCALE
    # ======================================================

    plt.subplot(
        2,
        4,
        2
    )

    plt.imshow(
        img_gray,
        cmap="gray"
    )

    plt.title(
        "Ảnh mức xám"
    )

    plt.axis(
        "off"
    )


    # ======================================================
    # 3. HISTOGRAM + PHƯƠNG SAI + NGƯỠNG OTSU
    # ======================================================

    ax_hist = plt.subplot(
        2,
        4,
        3
    )


    # Histogram
    ax_hist.plot(
        np.arange(256),
        histogram,
        label="Histogram"
    )


    ax_hist.set_title(
        "Histogram + Otsu"
    )

    ax_hist.set_xlabel(
        "Mức xám"
    )

    ax_hist.set_ylabel(
        "Số pixel"
    )

    ax_hist.set_xlim(
        [0, 255]
    )


    # Trục Y thứ hai
    ax_variance = ax_hist.twinx()


    # Phương sai giữa hai lớp
    ax_variance.plot(
        np.arange(256),
        variance_list,
        linestyle="--",
        label="σ²B(t)"
    )


    ax_variance.set_ylabel(
        "Phương sai giữa hai lớp"
    )


    # Đường ngưỡng tối ưu
    ax_variance.axvline(
        x=best_threshold,
        linestyle="-",
        linewidth=2,
        label=f"t* = {best_threshold}"
    )


    # Gộp legend
    lines1, labels1 = (
        ax_hist.get_legend_handles_labels()
    )

    lines2, labels2 = (
        ax_variance.get_legend_handles_labels()
    )

    ax_variance.legend(
        lines1 + lines2,
        labels1 + labels2,
        loc="upper right"
    )


    # ======================================================
    # 4. BINARY
    # ======================================================

    plt.subplot(
        2,
        4,
        4
    )

    plt.imshow(
        dst_binary,
        cmap="gray"
    )

    plt.title(
        f"1. Binary\nT = {best_threshold}"
    )

    plt.axis(
        "off"
    )


    # ======================================================
    # 5. BINARY INVERTED
    # ======================================================

    plt.subplot(
        2,
        4,
        5
    )

    plt.imshow(
        dst_binary_inv,
        cmap="gray"
    )

    plt.title(
        "2. Binary Inverted"
    )

    plt.axis(
        "off"
    )


    # ======================================================
    # 6. TRUNCATED
    # ======================================================

    plt.subplot(
        2,
        4,
        6
    )

    plt.imshow(
        dst_trunc,
        cmap="gray",
        vmin=0,
        vmax=255
    )

    plt.title(
        "3. Truncated"
    )

    plt.axis(
        "off"
    )


    # ======================================================
    # 7. TO ZERO
    # ======================================================

    plt.subplot(
        2,
        4,
        7
    )

    plt.imshow(
        dst_tozero,
        cmap="gray",
        vmin=0,
        vmax=255
    )

    plt.title(
        "4. To Zero"
    )

    plt.axis(
        "off"
    )


    # ======================================================
    # 8. TO ZERO INVERTED
    # ======================================================

    plt.subplot(
        2,
        4,
        8
    )

    plt.imshow(
        dst_tozero_inv,
        cmap="gray",
        vmin=0,
        vmax=255
    )

    plt.title(
        "5. To Zero Inverted"
    )

    plt.axis(
        "off"
    )


    # ======================================================
    # HIỂN THỊ
    # ======================================================

    plt.tight_layout()

    plt.show()