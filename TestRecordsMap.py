# Import what you need
import unittest
from RecordsMap import LocalRecord, RecordsMap
# Include unittests here. Focus on readability, including comments and docstrings.

class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        """testing that a localrecord is actually defined"""
        LR = LocalRecord((180, 0))

        self.assertEqual(LR.pos, (180, 0))
        self.assertEqual(LR.max, None)
        self.assertEqual(LR.min, None)
        self.assertEqual(LR.precision, 0)


        LR = LocalRecord((0, 0), 100.11, -1.55, 1)

        self.assertEqual(LR.pos, (0, 0))
        self.assertEqual(LR.max, 100.11)
        self.assertEqual(LR.min, -1.55)
        self.assertEqual(LR.precision, 1)

        print("LocalRecord test_init OK")


    def test_hash(self):
        """Test that the hash function works"""
        t1 = (180, 0)
        LR = LocalRecord(t1)
        hash_tup = hash(t1)
        self.assertEqual(hash(LR), hash_tup)

        t2 = (123, 456)
        LR = LocalRecord(t2)
        hash_tup = hash(t2)
        self.assertEqual(hash(LR), hash_tup)

        print("LocalRecord test_hash OK")


    def test_eq(self):
        """testing the __eq__ magic method for LocalRecord"""
        LR1 = LocalRecord((180, 0.49))
        LR2 = LocalRecord((180.1, 0))

        LR3 = LocalRecord((180.1, 0), None, None, 1)

        self.assertTrue(LR1 == LR2)
        self.assertFalse(LR1 == LR3)

        print("LocalRecord test_eq OK")

    def test_add_report(self):
        """Tests the add_report method from LocalRecord class"""
        LR = LocalRecord((180, 0.49)) #nothing in max / min
        
        LR.add_report(1)
        self.assertEqual(LR.max, 1)
        self.assertEqual(LR.min, 1)

        LR.add_report(100)
        self.assertEqual(LR.max, 100)
        self.assertEqual(LR.min, 1)

        LR.add_report(-1)
        self.assertEqual(LR.max, 100)
        self.assertEqual(LR.min, -1)

        LR.add_report(50)
        self.assertEqual(LR.max, 100)
        self.assertEqual(LR.min, -1)
        print("LocalRecord test_add_report OK")


#===============================================================================
#===============================================================================
#===============================================================================



class TestRecordsMap(unittest.TestCase):

    def test(self):
        """testing init, len, get, contains"""
        RM = RecordsMap()

        self.assertEqual(RM._len, 0)
        self.assertEqual(RM._n_buckets, 8)
        print("TestRecordsMap init OK")
        
        self.assertEqual(len(RM), 0)
        print("TestRecordsMap len OK")



    def test_add_one_report(self):
        """testing add_report for recordMaps single atribute"""
        RM = RecordsMap()
        pos = (0, 0)
        temp = 50
        RM.add_report(pos, temp)
        
        self.assertEqual(len(RM), 1)
        print("TestRecordsMap test_add_one_report OK")

        RM.add_report(pos, 1000) #update, not new pos
        self.assertEqual(len(RM), 1)

        RM.add_report((1, 1), 1) #new pos
        self.assertEqual(len(RM), 2)
        print("TestRecordsMap add a few OK")


        LR = LocalRecord(pos)
        self.assertTrue(LR in RM)
        print("TestRecordsMap contains OK")

        pos1 = (1, 2)
        RM.add_report(pos1, 10)
        self.assertEqual(RM[pos1], (10, 10))
        print("TestRecordsMap get OK")




    def test_add_many_reports(self):
        """testing add_report for recordMaps multiple additions, envoking rehash method in recordMaps"""
        RM = RecordsMap()
        for i in range(5): #should rehash the bucket length is greater than 2*bucket length
            RM.add_report((i, i), 0)

        self.assertEqual(len(RM), 5)
        self.assertEqual(RM._n_buckets, 16) 


        print("TestRecordsMap test_add_many_reports OK")



# You need to add a line here to run the unittests
unittest.main()