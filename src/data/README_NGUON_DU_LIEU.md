# Bộ nguồn dữ liệu Markdown về Văn kiện Đại hội XIV

Bộ dữ liệu gồm 4 tài liệu được chuyển đổi một-một từ PDF nguồn sang Markdown UTF-8. Cấu trúc tiêu đề, câu hỏi - trả lời, danh sách và mốc trang vật lý của PDF được giữ/chuẩn hóa để thuận lợi cho tìm kiếm toàn văn, chia đoạn và truy xuất dẫn chứng trong hệ thống RAG.

## Danh mục

- **Báo cáo tổng kết một số vấn đề lý luận và thực tiễn về công cuộc đổi mới theo định hướng xã hội chủ nghĩa trong 40 năm qua ở Việt Nam**
  - Tệp: `bao_cao_tong_ket_40_nam_doi_moi.md`
  - PDF nguồn: `bao_cao_ly_luan_1770390640065_260207_090802.pdf`
  - Số trang: 127
  - Phương pháp: trích xuất văn bản gốc

- **Nghị quyết số 71-NQ/TW của Bộ Chính trị về đột phá phát triển giáo dục và đào tạo**
  - Tệp: `nghi_quyet_71_dot_pha_phat_trien_giao_duc_va_dao_tao.md`
  - PDF nguồn: `NQ 71.pdf`
  - Số trang: 12
  - Phương pháp: OCR tiếng Việt 500 DPI có hiệu chỉnh

- **Phụ lục 5: Tổng kết công tác xây dựng Đảng nhiệm kỳ Đại hội XIII và phương hướng, nhiệm vụ, giải pháp công tác xây dựng Đảng nhiệm kỳ Đại hội XIV**
  - Tệp: `phu_luc_5_cong_tac_xay_dung_dang_nhiem_ky_dai_hoi_XIV.md`
  - PDF nguồn: `phu_luc_5_1770391058473_260207_090440.pdf`
  - Số trang: 31
  - Phương pháp: trích xuất văn bản gốc

- **Tài liệu hỏi - đáp về nội dung cơ bản của Văn kiện Đại hội đại biểu toàn quốc lần thứ XIV của Đảng**
  - Tệp: `tai_lieu_hoi_dap_noi_dung_co_ban_van_kien_dai_hoi_XIV.md`
  - PDF nguồn: `tai_lieu_hoi_dap_ve_noi_dung_cb_cua_cac_van_kien___260207_090400.pdf`
  - Số trang: 272
  - Phương pháp: giải mã phông chữ kế thừa và đối chiếu OCR

## Khuyến nghị nạp nguồn cho trợ lý AI

1. Sử dụng RAG/truy xuất tài liệu thay vì chỉ yêu cầu mô hình "ghi nhớ" toàn văn.
2. Chia đoạn theo tiêu đề Markdown, khoảng 700-1.200 token; chồng lấn 100-150 token.
3. Gắn metadata cho từng đoạn: `title`, `source_pdf`, `page`, tiêu đề mục/câu hỏi và loại văn bản.
4. Khi trả lời, buộc hệ thống nêu tên tài liệu và trang; không suy diễn vượt quá nội dung được truy xuất.
5. Thiết lập thứ tự ưu tiên: tài liệu hỏi - đáp Văn kiện Đại hội XIV -> báo cáo/phụ lục Văn kiện -> nghị quyết chuyên đề trực tiếp liên quan.
6. Với trích dẫn nguyên văn, số liệu, mốc thời gian hoặc nội dung dùng để công bố chính thức, đối chiếu lại PDF nguồn. Điều này đặc biệt quan trọng đối với `NQ 71.pdf`, là tài liệu ảnh quét được OCR.

## Định dạng mốc trang

Mỗi trang bắt đầu bằng chú thích dạng:

```markdown
<!-- page: 25 -->
```

Mốc này là số trang vật lý của PDF, không nhất thiết trùng với số trang in trên tài liệu do có bìa và trang lót.
