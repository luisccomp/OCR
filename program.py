from json import dumps

from services.ocr_service import extract_document_info, extract_driver_license_info


if __name__ == "__main__":
    # data = extract_document_info("images/RG_full.jpg", False)
    data = extract_driver_license_info('images/cnh_full.jpg', False)

    print(dumps(data, ensure_ascii=False, indent=2))
