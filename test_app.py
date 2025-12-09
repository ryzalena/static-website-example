def test_files_exist():
    """Проверяем наличие необходимых файлов"""
    assert os.path.exists("app.py"), "app.py должен существовать"
    
def test_requirements():
    """Проверяем наличие requirements.txt"""
    assert os.path.exists("requirements.txt"), "requirements.txt должен существовать"
    
def test_simple():
    """Простой тест для проверки работы pytest"""
    assert 1 + 1 == 2
