import unittest
from db import db_manager

class TestSQLI(unittest.TestCase):
        
    sqli_test = "'abc;--#"

    def test_smartmeter_register(self):
        self.assertIsNone(db_manager.smartmeter_register(self.sqli_test, self.sqli_test, self.sqli_test, self.sqli_test))

    def test_smartmeter_data(self):
        self.assertIsNone(db_manager.smartmeter_data(self.sqli_test, self.sqli_test, self.sqli_test, self.sqli_test))
    
    def test_supplier_reading_history(self):
        self.assertIsInstance(db_manager.supplier_reading_history(self.sqli_test), list)
    
    def test_supplier_reading_current(self):
        self.assertIsInstance(db_manager.supplier_reading_current(self.sqli_test), tuple)

    def test_supplier_smartmeter(self):
        self.assertIsInstance(db_manager.supplier_smartmeter(self.sqli_test), list)

    def test_frontend_smartmeter_getAllMeterData(self):
        self.assertIsInstance(db_manager.frontend_smartmeter_getAllMeterData(self.sqli_test), list)

    def test_frontend_smartmeter_supplier(self):
        self.assertTrue(isinstance(tmp := db_manager.frontend_smartmeter_supplier(self.sqli_test), tuple) or tmp == None)

    def test_frontend_supplier_smartmeter(self):
        self.assertIsInstance(db_manager.frontend_supplier_smartmeter(self.sqli_test), list)

    def test_frontend_supplier_add(self):
        self.assertIsNone(db_manager.frontend_supplier_add(self.sqli_test, self.sqli_test, self.sqli_test))

    def test_frontend_supplier_assign(self):
        self.assertIsNone(db_manager.frontend_supplier_assign(self.sqli_test, self.sqli_test))

    def test_check_supplier_owns_reader(self):
        self.assertIsInstance(db_manager.check_supplier_owns_reader(self.sqli_test, self.sqli_test), bool)




if __name__ == "__main__":
    unittest.main()