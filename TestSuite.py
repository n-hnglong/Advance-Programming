import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):
    def test_0(self):
        input = ["INSERT a1 number", "INSERT b2 string"]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 100))

    def test_1(self):
        input = ["INSERT x number", "INSERT y string", "INSERT x string"]
        expected = ["Redeclared: INSERT x string"]

        self.assertTrue(TestUtils.check(input, expected, 101))

    def test_2(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "ASSIGN x 15",
            "ASSIGN y 17",
            "ASSIGN x 'abc'",
        ]
        expected = ["TypeMismatch: ASSIGN y 17"]

        self.assertTrue(TestUtils.check(input, expected, 102))

    def test_3(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "END",
            "END",
        ]
        expected = ["success", "success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 103))

    def test_4(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "LOOKUP x",
            "LOOKUP y",
            "END",
        ]
        expected = ["success", "success", "success", "1", "0"]

        self.assertTrue(TestUtils.check(input, expected, 104))

    def test_5(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "PRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "y//0 x//1 z//1"]

        self.assertTrue(TestUtils.check(input, expected, 105))

    def test_6(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "INSERT z number",
            "RPRINT",
            "END",
        ]
        expected = ["success", "success", "success", "success", "z//1 x//1 y//0"]

        self.assertTrue(TestUtils.check(input, expected, 106))

    def test_7(self):
        input = [
            "    INSERT x number"
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 107))

    def test_8(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "BEGIN",
            "INSERT y string",
            "END"
        ]
        expected = ["UnclosedBlock: 1"]

        self.assertTrue(TestUtils.check(input, expected, 108))

    def test_9(self):
        input = [
            "END",
            "END",
        ]
        expected = ["UnknownBlock"]

        self.assertTrue(TestUtils.check(input, expected, 109))

    def test_10(self):
        input = [
            "INSERT x number",
            "ASSIGN x y",
        ]
        expected = ["Undeclared: ASSIGN x y"]

        self.assertTrue(TestUtils.check(input, expected, 110))

    def test_11(self):
        input = [
            "INSERT x number",
            "ASSIGN x x",
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 111))

    def test_12(self):
        input = [
            "INSERT x number",
            "INSERT y string",
            "BEGIN",
            "INSERT x number",
            "BEGIN",
            "INSERT y string"
        ]
        expected = ["UnclosedBlock: 2"]

        self.assertTrue(TestUtils.check(input, expected, 112))

    def test_13(self):
        input = [
            "INSERT x string",
            "ASSIGN x 'a@1'",
        ]
        expected = ["Invalid: ASSIGN x 'a@1'"]

        self.assertTrue(TestUtils.check(input, expected, 113))

    def test_14(self):
        input = [
            "BEGIN 3"
        ]
        expected = ["Invalid: BEGIN 3"]

        self.assertTrue(TestUtils.check(input, expected, 114))

    def test_15(self):
        input = [
            "INSERT abc 456   "
        ]
        expected = ["Invalid: INSERT abc 456   "]

        self.assertTrue(TestUtils.check(input, expected, 115))

    def test_16(self):
        input = [
            "INSERT x  string"
        ]
        expected = ["Invalid: INSERT x  string"]

        self.assertTrue(TestUtils.check(input, expected, 116))

    def test_17(self):
        input = [
            ""
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 117))

    def test_18(self):
        input = [
            "INSERT a number",
            "LOOKUP a"
        ]
        expected = ["success", "0"]

        self.assertTrue(TestUtils.check(input, expected, 118))

    def test_19(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT b string",
            "LOOKUP a",
            "LOOKUP b",
            "END",
            "LOOKUP a"
        ]
        expected = ["success", "success", "0", "1", "0"]

        self.assertTrue(TestUtils.check(input, expected, 119))

    def test_20(self):
        input = [
            "INSERT a number",
            "LOOKUP 1a"
        ]
        expected = ["Invalid: LOOKUP 1a"]

        self.assertTrue(TestUtils.check(input, expected, 120))

    def test_21(self):
        input = [
            "INSERT a number",
            "LOOKUP b"
        ]
        expected = ["Undeclared: LOOKUP b"]

        self.assertTrue(TestUtils.check(input, expected, 121))

    def test_22(self):
        input = [
            "INSERT @@@ number",
            "LOOKUP @@@"
        ]
        expected = ["Invalid: INSERT @@@ number"]

        self.assertTrue(TestUtils.check(input, expected, 122))

    def test_23(self):
        input = [
            "BEGIN",
            "BEGIN",
            "END",
            "END"
        ]
        expected = []

        self.assertTrue(TestUtils.check(input, expected, 123))

    def test_24(self):
        input = [
            "INSERT number number",
            "ASSIGN number number"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 124))

    def test_25(self):
        input = [
            "INSERT number number",
            "ASSIGN number number",
            "INSERT string number",
            "ASSIGN string number"
        ]
        expected = ["success", "success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 125))

    def test_26(self):
        input = [
            "INSERT number number",
            "BEGIN",
            "INSERT number string",
            "END",
            "ASSIGN number 1"
        ]
        expected = ["success", "success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 126))

    def test_27(self):
        input = [
            "INSERT a number",
            "INSERT b string",
            "PRINT",
            "RPRINT"
        ]
        expected = ["success", "success", "a//0 b//0", "b//0 a//0"]

        self.assertTrue(TestUtils.check(input, expected, 127))

    def test_28(self):
        input = [
            "INSERT a number",
            "BEGIN",
            "INSERT b string",
            "PRINT",
            "RPRINT",
            "END",
            "PRINT",
            "RPRINT"
        ]
        expected = ["success", "success", "a//0 b//1", "b//1 a//0", "a//0", "a//0"]

        self.assertTrue(TestUtils.check(input, expected, 128))

    def test_29(self):
        input = [
            "INSERT x number",
            "BEGIN",
            "PRINT",
            "END",
            "LOOKUP y"
        ]
        expected = ["Undeclared: LOOKUP y"]

        self.assertTrue(TestUtils.check(input, expected, 129))

    def test_30(self):
        input = [
            "PRINT",
            "RPRINT",
            "BEGIN",
            "END",
            "PRINT",
            "PRINT"
        ]
        expected = ["","","",""]

        self.assertTrue(TestUtils.check(input, expected, 130))

    def test_31(self):
        input = [
            "INSERT a1b2c3d4e5 string"
        ]
        expected = ["success"]

        self.assertTrue(TestUtils.check(input, expected, 131))

    def test_32(self):
        input = [
            "LOOKUP xyz",
            "LOOKUP def"
        ]
        expected = ["Undeclared: LOOKUP xyz"]

        self.assertTrue(TestUtils.check(input, expected, 132))

    def test_33(self):
        input = [
            "END",
            "BEGIN",
            "END",
            "BEGIN"
        ]
        expected = ["UnknownBlock"]

        self.assertTrue(TestUtils.check(input, expected, 133))

    def test_34(self):
        input = [
            "BEGIN",
            "END",
            "BEGIN",
            "END",
            "BEGIN"
        ]
        expected = ["UnclosedBlock: 1"]

        self.assertTrue(TestUtils.check(input, expected, 134))

    def test_35(self):
        input = [
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "BEGIN",
            "BEGIN"
        ]
        expected = ["UnclosedBlock: 5"]

        self.assertTrue(TestUtils.check(input, expected, 135))

    def test_36(self):
        input = [
            "INSERT z number",
            "INSERT y string",
            "INSERT x number",
            "BEGIN",
            "INSERT c number",
            "INSERT b string",
            "INSERT a number",
            "PRINT",
            "RPRINT"
        ]
        expected = ["UnclosedBlock: 1"]

        self.assertTrue(TestUtils.check(input, expected, 136))

    def test_37(self):
        input = [
            "INSERT z number",
            "INSERT y string",
            "INSERT x number",
            "BEGIN",
            "INSERT c number",
            "INSERT b string",
            "INSERT a number",
            "PRINT",
            "RPRINT",
            "END"
        ]
        expected = ["success", "success", "success", "success", "success", "success", "z//0 y//0 x//0 c//1 b//1 a//1", "a//1 b//1 c//1 x//0 y//0 z//0"]

        self.assertTrue(TestUtils.check(input, expected, 137))

    def test_38(self):
        input = [
            "INSERT a1 string",
            "ASSIGN a1 a1"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 138))

    def test_39(self):
        input = [
            "INSERT a1 string",
            "ASSIGN a1 'a1'"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 139))

    def test_40(self):
        input = [
            "INSERT a1 number",
            "ASSIGN a1 'a1'"
        ]
        expected = ["TypeMismatch: ASSIGN a1 'a1'"]

        self.assertTrue(TestUtils.check(input, expected, 140))

    def test_41(self):
        input = [
            "INSERT a1 string",
            "ASSIGN a1 a2a3a4"
        ]
        expected = ["Undeclared: ASSIGN a1 a2a3a4"]

        self.assertTrue(TestUtils.check(input, expected, 141))

    def test_42(self):
        input = [
            "INSERT a1 string",
            "ASSIGN a1 ''"
        ]
        expected = ["success", "success"]

        self.assertTrue(TestUtils.check(input, expected, 142))

    def test_43(self):
        input = [
            "INSERT a1 string",
            "ASSIGN a1"
        ]
        expected = ["Invalid: ASSIGN a1"]

        self.assertTrue(TestUtils.check(input, expected, 143))

    def test_44(self):
        input = [
            "INSERT a1xyz number",
            "ASSIGN a1xyz 555       "
        ]
        expected = ["Invalid: ASSIGN a1xyz 555       "]

        self.assertTrue(TestUtils.check(input, expected, 144))

    def test_45(self):
        input = [
            "INSERT 2345var000 number",
            "LOOKUP 2345var000"
        ]
        expected = ["Invalid: INSERT 2345var000 number"]

        self.assertTrue(TestUtils.check(input, expected, 145))

    def test_46(self):
        input = [
            "INSERT def number",
            " LOOKUP def"
        ]
        expected = ["Invalid: Invalid command"]

        self.assertTrue(TestUtils.check(input, expected, 146))

    def test_47(self):
        input = [
            "INSERT x string",
            "ASSIGN x ''''"
        ]
        expected = ["Invalid: ASSIGN x ''''"]

        self.assertTrue(TestUtils.check(input, expected, 147))

    def test_48(self):
        input = [
            "INSERT x2 string",
            "ASSIGN x2 'done'",
            "INSERT x2 string",
            "ASSIGN x2 'done'",
        ]
        expected = ["Redeclared: INSERT x2 string"]

        self.assertTrue(TestUtils.check(input, expected, 148))

    def test_49(self):
        input = []
        expected = []

        self.assertTrue(TestUtils.check(input, expected, 149))

    
    
    

    
    

    
    
