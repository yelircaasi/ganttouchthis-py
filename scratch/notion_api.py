import random
import time
from datetime import date

# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options as FirefoxOptions

# from selenium import webdriver
# from notion import NotionClient
# #notion = NotionClient(auth="secret_puQIMI4ybuvo12k5l9BX0QSLWzh26GSqufCAVO1bPCw")
# notion = NotionClient(auth="secret_fdf83SxJcqjaOfkyt8bz0CUfZt63ziydbVAbNRa1a48")
# #notion.pages.retrieve("efc46201-9551-46a9-9399-e6d4bad3c356")
# notion.pages.retrieve("10e2a531-d363-41da-85f8-5410a07749de")

# from notion_client import Client
# notion = Client(auth="secret_puQIMI4ybuvo12k5l9BX0QSLWzh26GSqufCAVO1bPCw")
# b = notion.blocks.retrieve("6dff26afe08a4904b75c5bb356512f6a")
# #notion.blocks.update("6dff26afe08a4904b75c5bb356512f6a", to_do={"rich_text": [{"text": {"content": "Lacinato kale"}}], "checked": false})

# tu1100 = "af8c95c60aba414ebb349713c4f3a641"
# b = notion.blocks.retrieve(tu1100)
# update = {'rich_text': [{'type': 'mention',
#                          'mention': {'type': 'date',
#                                      'date': {'start': '2023-03-07T11:00:00.000+01:00',
#                                               'end': None,
#                                               'time_zone': None}},
#                          'annotations': {'bold': True,
#                                          'italic': False,
#                                          'strikethrough': False,
#                                          'underline': False,
#                                          'code': False,
#                                          'color': 'default'},
#                          'plain_text': '2023-01-31T11:00:00.000+01:00',
#                          'href': None},
#                         {'type': 'text',
#                          'text': {'content': ' \n', 'link': None},
#                          'annotations': {'bold': True,
#                                          'italic': False,
#                                          'strikethrough': False,
#                                          'underline': False,
#                                          'code': False,
#                                          'color': 'default'},
#                          'plain_text': ' \n',
#                          'href': None}],
#           'checked': False,
#           'color': 'default'}

# notion.blocks.update(tu1100, to_do=update)
DAY_BLOCK_IDS: {
    (-1, 5): "a4762977e5fd4288858f9477aced2d0e",
    (-1, 6): "0fd8650174234d4eb092a63771659b17",
    (-1, 7): "e1c413b30c3440a48f708c415163de7b",
    (0, 1): "18fbfaaa7ee44cc39745131a1eb869ad",
    (0, 2): "0dbf9ab882bd42b38e7aa389b8d80361",
    (0, 3): "3c6a7b5f93114538b977733b8501e0a7",
    (0, 4): "56673c6e4fcb4dadab7416432fcd4199",
    (0, 5): "d5b4c0b1d4c3426498dd4ec1e5a69504",
    (0, 6): "0d4aacdb5d904e0dbdb22cb4806f63da",
    (0, 7): "f320ee1e513443339103380451b71872",
}

TIME_BLOCK_IDS = {
    (-1, 5, 4, 0): "53e6453be1be4c36a2c47c4706771bc7",
    (-1, 5, 4, 30): "508ec993475e4b4caaa2f444b6a2b61a",
    (-1, 5, 5, 0): "7d9654d050964c8fb89a28e98b2f5b6d",
    (-1, 5, 5, 30): "73c4ad2c9f9d4758bec542837132a1a2",
    (-1, 5, 6, 0): "6b32e2fba18f49aeae2721b85e7dd4e1",
    (-1, 5, 6, 30): "470f508037a642c1853e8c9a29b9be55",
    (-1, 5, 7, 0): "f6ac02c813b9445ab42429a112fdc146",
    (-1, 5, 7, 30): "8706b040a31b4d4aaa6330f5105b2898",
    (-1, 5, 8, 0): "81b8d3cf53e54069ab0fe1972c6b80f4",
    (-1, 5, 8, 30): "873776abcd274b79a88ba286a1b105d2",
    (-1, 5, 9, 0): "4288a61cd73149aba1bcc08c5ac37e87",
    (-1, 5, 9, 30): "f39cbfd3bcee4705a59c81b394f71050",
    (-1, 5, 10, 0): "7f53cb729e28444f96d257da96cb0a26",
    (-1, 5, 10, 30): "7eba0c3f42f3443699ffe17b8da2888b",
    (-1, 5, 11, 0): "761cb07dd0204e1da270e896709e60f7",
    (-1, 5, 11, 30): "c37876d184db46c3917360382422d15f",
    (-1, 5, 12, 0): "a11a67be4812486095e0c55dfac718a9",
    (-1, 5, 12, 30): "fe4b6dc6b2774536a18623c32db3df1c",
    (-1, 5, 13, 0): "019226cc742d4dd2a3896b1cc9293f2a",
    (-1, 5, 13, 30): "8fe0c7bee98449148596e7606ce7e889",
    (-1, 5, 14, 0): "0c76173911be4ad69817c18a6868e802",
    (-1, 5, 14, 30): "4d2b2fc2ba414d9bb586d373e995bcdf",
    (-1, 5, 15, 0): "d66daf00578e4c438e403651ef63d326",
    (-1, 5, 15, 30): "3229273d880d47fc965610478afcdd23",
    (-1, 5, 16, 0): "ec283b36889c4298a73754095f9ba48b",
    (-1, 5, 16, 30): "7921729a9a8c4198b1509129badfc4f1",
    (-1, 5, 17, 0): "d6be2606ddd64b8daad6bc568f019cf8",
    (-1, 5, 17, 30): "57a3b70ad5424f178d08f662780dc515",
    (-1, 5, 18, 0): "315992821e5a42b1864343197d5aff1c",
    (-1, 5, 18, 30): "2a9c2dae6937473db87ab01d21b2ab0e",
    (-1, 5, 19, 0): "27f38670773844acb90aaa11a7ad9acf",
    (-1, 5, 19, 30): "c388704aa0be4509b00d867e6a4c88e4",
    (-1, 5, 20, 0): "ae80c56ae6774896a4dd9eb596f69ab9",
    (-1, 5, 20, 30): "8c41274a56984cbf8c14159905b09c52",
    (-1, 5, 21, 0): "3c0550979bec4333a4cfe6c9e34f2e03",
    (-1, 5, 21, 30): "65de66d5add74dd189fc4aaf5efe951f",
    (-1, 5, 22, 0): "4615974b20fc4b269e4f4f1d5f3e4db1",
    (-1, 5, 22, 30): "ea274bcc1bda43bd80bf49a83c2f98ae",
    (-1, 5, 23, 0): "7b46bcae5f4149ef88828726850bf9c4",
    (-1, 5, 23, 30): "4a37de07afdc4a9bab30528cd277d627",
    (-1, 6, 4, 0): "4447fec4edea4233b966040946f267e7",
    (-1, 6, 4, 30): "761e0e94045144b58b5203b206f0009b",
    (-1, 6, 5, 0): "be5ab26fffca4a3da2b63163f5dcc7cf",
    (-1, 6, 5, 30): "9a769e002e4e46bfaccdf2ad5b6f4fd7",
    (-1, 6, 6, 0): "974880b3f61e4315a66a3b96e9d71e8c",
    (-1, 6, 6, 30): "4c990fab0d9c4d80b48092abd04a920d",
    (-1, 6, 7, 0): "f9d96795649e4d02a5e95f3dd8fdbbe6",
    (-1, 6, 7, 30): "e67015809e5842dab9e46fc3477c707c",
    (-1, 6, 8, 0): "cee3715fc2834acbaa17835b25e63c07",
    (-1, 6, 8, 30): "cfbef6df20f54d48bdcf54ba4325994a",
    (-1, 6, 9, 0): "47a6141ad4f547549ed5545567ea734d",
    (-1, 6, 9, 30): "b84b352b2ea84e258ab635376216a8a2",
    (-1, 6, 10, 0): "cd65644f68844b549833c137a4d27755",
    (-1, 6, 10, 30): "674f5140528f4adab4f8f4ee613fd39c",
    (-1, 6, 11, 0): "f677cf7512764023a41b146c4dd2867c",
    (-1, 6, 11, 30): "c78f064f63394d61a38a92620d8f86a2",
    (-1, 6, 12, 0): "53fe819b6f24492caf8dfd9c2cd9cf5a",
    (-1, 6, 12, 30): "d040a50ab92046faa49f8800c20640fa",
    (-1, 6, 13, 0): "8db313785f204bea9c131b24b1bf153b",
    (-1, 6, 13, 30): "f49dcabb2a8b42b1b22512579fdf2287",
    (-1, 6, 14, 0): "8d3cc447d7634c36a2116e5e7cd2c6d5",
    (-1, 6, 14, 30): "5791c01aeb0c44cf875d1746a78fa47f",
    (-1, 6, 15, 0): "64565cea06cf40d49936b21909586dd8",
    (-1, 6, 15, 30): "9dafe7158c63421789b98a02a3454ce4",
    (-1, 6, 16, 0): "351e7cb6dadc419282242403cd173535",
    (-1, 6, 16, 30): "efdaf91fbfa94d2fb268306bf51ab637",
    (-1, 6, 17, 0): "a62582ac2a8d437a8b9fc15d18395991",
    (-1, 6, 17, 30): "ba5558f76a734a94acc946de69cbc31c",
    (-1, 6, 18, 0): "61e96eaf3ffb44e08a6f9eb2b7c78305",
    (-1, 6, 18, 30): "185c13e95db14488af68812422befd15",
    (-1, 6, 19, 0): "94e974785b10471ca182ad4f4934ecf4",
    (-1, 6, 19, 30): "34a7ffde1a3145b4be801082fe795dd7",
    (-1, 6, 20, 0): "1656b3978e27438cac9d5de2dad0ad31",
    (-1, 6, 20, 30): "6422317527ce4884a9f68aa8ae89bdaf",
    (-1, 6, 21, 0): "baf3059e21a84afb8cf98029b75835e9",
    (-1, 6, 21, 30): "265acdb06ba6459fbc1d7694b9104421",
    (-1, 6, 22, 0): "34a8b8fdc2604737afa931b094a5df45",
    (-1, 6, 22, 30): "1643da6862c04ef3a9577815cb8a2ea6",
    (-1, 6, 23, 0): "d2941f28f216485d9039ed0cfbe995fc",
    (-1, 6, 23, 30): "de0a56e00d5f4e5cb671a3160eb39556",
    (-1, 7, 4, 0): "bfd597dc025b4ccd9972b8a3f2504d40",
    (-1, 7, 4, 30): "e409aa6727b24aa1b2102fa6522d778d",
    (-1, 7, 5, 0): "caffb8002b9a498e938ae3b72a57f766",
    (-1, 7, 5, 30): "80c01740f26849e792251bb8578fc0f3",
    (-1, 7, 6, 0): "7876fd590dd34d86b88a4ee358dadc30",
    (-1, 7, 6, 30): "6e997a8085e04940a408a54919caaf67",
    (-1, 7, 7, 0): "b188de5050d54f00820c2ab7f8f66bfe",
    (-1, 7, 7, 30): "6a3be9faa63740d2be7a354bde375ef9",
    (-1, 7, 8, 0): "ad39ee3047e74158b3c79716425e502e",
    (-1, 7, 8, 30): "fae6d818ff2e4f4b900a2deb09ed2d40",
    (-1, 7, 9, 0): "5471ff794fe34584a2173a06158c6b85",
    (-1, 7, 9, 30): "d8af5bfe9ee34bd597223bad1f2f58f2",
    (-1, 7, 10, 0): "2f517a781caf47179d04623a152afc73",
    (-1, 7, 10, 30): "2fdb14d0819741cea970e7f368f34e68",
    (-1, 7, 11, 0): "21da392a02324a54b91bc716e3957b18",
    (-1, 7, 11, 30): "f156ae84c00a404e9a0fd6ab736741e7",
    (-1, 7, 12, 0): "9fcde0b2fd0b4517b29171c55cfbeedc",
    (-1, 7, 12, 30): "3b92b9b4afb3418ea1c08e8c6b62b5cb",
    (-1, 7, 13, 0): "53cb348b679e4baca1cf0e0e170817ec",
    (-1, 7, 13, 30): "ff88bf439bb34325b08557771aec2847",
    (-1, 7, 14, 0): "e0c43950d9cb44e39a171214ecb850e3",
    (-1, 7, 14, 30): "a3310361343c4a7fa3f7b96897096754",
    (-1, 7, 15, 0): "d598c47d40ad4a1dac80f1b9c381b436",
    (-1, 7, 15, 30): "e0d9db64bee340e08ee820c2a2eb1a89",
    (-1, 7, 16, 0): "3ea3b01fc1a84c34a1d3ffd72b2c5230",
    (-1, 7, 16, 30): "913cf7e98dd84ab48c95ee67dfe35108",
    (-1, 7, 17, 0): "777c168fd8d84820ad4f1abd9e6e2ecb",
    (-1, 7, 17, 30): "4305367173384440970e8485880eff26",
    (-1, 7, 18, 0): "fe85f8398e304c079ad6b28d44a2a29d",
    (-1, 7, 18, 30): "65821813fcca44a28f3a3533f0df0960",
    (-1, 7, 19, 0): "73469cfb785b44dbae59f64e9e4c129d",
    (-1, 7, 19, 30): "f965481d2e9e463385b449e276556668",
    (-1, 7, 20, 0): "7fa9ccec6c1448829a3b77aebbf835a6",
    (-1, 7, 20, 30): "57840ab9a25c40c5954a72f3797dd5e3",
    (-1, 7, 21, 0): "2664f6f3c3494e968a225327a3ed55b0",  # "2664f6f3c3494e968a225327a3ed55b0",
    (-1, 7, 21, 30): "8e35b1983e194d3c86805841a440439d",
    (-1, 7, 22, 0): "eea9511ca1bc4a368417cb760bafdfe2",
    (-1, 7, 22, 30): "378ab83ee81148a9bba78a826af562aa",
    (-1, 7, 23, 0): "b2c1c0914c2e42c799bec7c5f6930e01",
    (-1, 7, 23, 30): "fb8209b4cce745e392bca90b412015b5",
    (0, 1, 4, 0): "692d208abfc54eb7b35d86beeb2fcb61",
    (0, 1, 4, 30): "8aaf05da60e643dfb75e07f3acd49ed2",
    (0, 1, 5, 0): "aae1205a094c4a339b9f826255284aa3",
    (0, 1, 5, 30): "1a31dc573c2541959bd253f5e898598f",
    (0, 1, 6, 0): "291b2a461c7a4e37b90ac7d251620896",
    (0, 1, 6, 30): "5d5539956d6c4c6d88f4c29dbf514f75",
    (0, 1, 7, 0): "d52418bb276f41b99723e8a41334e8d4",
    (0, 1, 7, 30): "b0b181cbd1fb4c2aadb32674bdbc01b2",
    (0, 1, 8, 0): "55f71445952a44ceb9b9bd1b95aec476",
    (0, 1, 8, 30): "45c900e15122431b91dec748aa309a04",
    (0, 1, 9, 0): "871946884cec4bac8c7b46e716658548",
    (0, 1, 9, 30): "88379bf951574ef3bc55e8852785e10f",
    (0, 1, 10, 0): "2405ed30e4914b85b3aaee9b3eef8dc2",
    (0, 1, 10, 30): "d204f6c2df5b41d3bd8df02e3669089f",
    (0, 1, 11, 0): "a1c38dbc474c41e7822465c2b9fc9ec3",
    (0, 1, 11, 30): "421b910eec684a9fbfc418f027472983",
    (0, 1, 12, 0): "fd53db90999c44ed9281b1533b821315",
    (0, 1, 12, 30): "107a98767a254dd6822922c2bd550452",
    (0, 1, 13, 0): "871ec19b3b2c4176b9f22abb8b499f8b",
    (0, 1, 13, 30): "a7e50f1c76414fa68d88f61de9c64bcc",
    (0, 1, 14, 0): "ee0bf52d60af409cb88ba0860e43ef55",
    (0, 1, 14, 30): "27fc8cd8726c4183bbb3bf52ce4405ad",
    (0, 1, 15, 0): "00d5abb5ba524c99a5cc8b6d863a3ea4",
    (0, 1, 15, 30): "e3dff9ae68564a27898b0a85d081608f",
    (0, 1, 16, 0): "ea5545e04a7b413f8a16fdc8d9f33cec",
    (0, 1, 16, 30): "5c416a01f1684cb5ad026dc49d941396",
    (0, 1, 17, 0): "926b809e0cfb49bdad6ac951612e45a0",
    (0, 1, 17, 30): "cfc29d3c4c584062b39287fd3e26d3df",
    (0, 1, 18, 0): "cfe0af511a9c4edab819bae70f9e75c1",
    (0, 1, 18, 30): "fdb9268a2b254b899bbbc9e9ea03f8a1",
    (0, 1, 19, 0): "0d6c402c60fe4f3a80461f2deea2e1dd",
    (0, 1, 19, 30): "004b49b109cf476d832b11276ccf4c14",
    (0, 1, 20, 0): "14e394dc285f4aa7a63a35b83e4a304f",
    (0, 1, 20, 30): "f5c1d138a9b843c1b0e238b6ce00aa4d",
    (0, 1, 21, 0): "f5b3d47b027f42d2bde974de02a894cb",
    (0, 1, 21, 30): "fd25e2f9f5bf45c7af6b8db49ed9a4e6",
    (0, 1, 22, 0): "6891a8b28a1840f6a0679fb3f791ef4f",
    (0, 1, 22, 30): "eee99dfc87a048c5ba89706ec1a66415",
    (0, 1, 23, 0): "d30232e4feb748aab0d25e63e6107a10",
    (0, 1, 23, 30): "d992e7ee1f0e4eab9d101a709857734f",
    (0, 2, 4, 0): "d76423748ade4731933918e3fa56dd84",
    (0, 2, 4, 30): "025726863b754bd5bd00d3b9cc421e00",
    (0, 2, 5, 0): "772544b386f849e98f04e5807d51d3d4",
    (0, 2, 5, 30): "df9c0da1a2a64154b2c89f52d44e1a70",
    (0, 2, 6, 0): "e5f539cf37d54c97a9cb3409ee1fb64d",
    (0, 2, 6, 30): "8811cd6043b542a4ac1c7b6d0254eadc",
    (0, 2, 7, 0): "5dac3b5e8c254faba1b5f243131b1689",
    (0, 2, 7, 30): "1e873fae49d94bc6b8a217cb7ecb2d6b",
    (0, 2, 8, 0): "2d1b85e379fd4dff99bb518d6ff0a9bf",
    (0, 2, 8, 30): "b435dc165df94ec9ba618057b5dcc5e2",
    (0, 2, 9, 0): "b91277960e174345b7712b9f1c231b7c",
    (0, 2, 9, 30): "2cad508eb9b24e3cb5cf640296aae031",
    (0, 2, 10, 0): "77ed66f1c950455aa27e954fcdb9bd8a",
    (0, 2, 10, 30): "b394f20f7d1049369bd9994b14d7712b",
    (0, 2, 11, 0): "af8c95c60aba414ebb349713c4f3a641",
    (0, 2, 11, 30): "fe2cf360406c4cbb97b33256c4704f10",
    (0, 2, 12, 0): "f0ce82c45dd74e54bdc16dd945495b09",
    (0, 2, 12, 30): "70e5b9873246476bbcc33860a18f2691",
    (0, 2, 13, 0): "b8e2fbe51a464b41bfa583439c526e0d",
    (0, 2, 13, 30): "e0e719ecb1034350a7515d730a4431f4",
    (0, 2, 14, 0): "fbfa81c4bec243aaa624f6df3c8c7736",
    (0, 2, 14, 30): "972c8e80add946ee8edab50bb5ef6748",
    (0, 2, 15, 0): "2a1443a80d1142cbadeebcaa5c3a07ba",
    (0, 2, 15, 30): "17d732c8b7464194bfc2e495b4538663",
    (0, 2, 16, 0): "d1b1ebb08fee4042b61952121b7a7d9d",
    (0, 2, 16, 30): "6c79704b5e7d46daa274ddda8386e562",
    (0, 2, 17, 0): "dff1372739ea4bfaace46d0041b1bd4f",
    (0, 2, 17, 30): "e1335b8c15f94418b5ebd4b04857b8b6",
    (0, 2, 18, 0): "19ff015d1f864b58bfcc960cc97447ec",
    (0, 2, 18, 30): "b0bcfa4ad5eb4b4ab0d8de5b37df8035",
    (0, 2, 19, 0): "3d9a8433977744a1adb2402968d1d776",
    (0, 2, 19, 30): "93381e5209fb498eae63bd1cb71219ab",
    (0, 2, 20, 0): "a81a65f9bf944a7fbc7b836892916fa3",
    (0, 2, 20, 30): "79800fdca8814f84a602a864a0dc492d",
    (0, 2, 21, 0): "1f26e25868c64a3aa70e5c258261a17b",
    (0, 2, 21, 30): "7d21ebb533c74658ac019c8b4c70a401",
    (0, 2, 22, 0): "58aff6918c21470bb809a9e7819eff15",
    (0, 2, 22, 30): "33e796d8e943473c92c85cc7f3b7895b",
    (0, 2, 23, 0): "0c1ceeda422844ceba1259038c2ae4a3",
    (0, 2, 23, 30): "f21c5b1efd2d4567b8f67de843be8119",
    (0, 3, 4, 0): "dc6ffa65f59a4a3ab8ef2ea0c5b5ba9c",
    (0, 3, 4, 30): "105a2930356147dea6e8b8c2b8fd9583",
    (0, 3, 5, 0): "aa630514612a44eb94dd5657ca5b83d8",
    (0, 3, 5, 30): "89168b5668ff4872899d2c62bee0f47f",
    (0, 3, 6, 0): "985135f77cd3451a887759005b74eb86",
    (0, 3, 6, 30): "b9951e9563964354ab7c9fc39a38e69d",
    (0, 3, 7, 0): "b09bb030845d4e4e85064e3aca42c945",
    (0, 3, 7, 30): "572926a9e51b4b5c8e5157b398ed0e6b",
    (0, 3, 8, 0): "b506f374b4554541b166f88656d847a1",
    (0, 3, 8, 30): "8d6bef88592c4c7f931dbab66b4b3ac5",
    (0, 3, 9, 0): "5e5aa32cf18c4628b95af65a56a2fe77",
    (0, 3, 9, 30): "7de9552ce60f4033b886fe61d390a578",
    (0, 3, 10, 0): "833d37e595c2457b8914f9dbdaf4e343",
    (0, 3, 10, 30): "d239c37e92fa46dd9d0630104194efd5",
    (0, 3, 11, 0): "78276b1da5224a22a4d8740d1b363e73",
    (0, 3, 11, 30): "a4932036b0944ac498dd5466ba46d33e",
    (0, 3, 12, 0): "70f9abf4ca0f4127a3518948ed258365",
    (0, 3, 12, 30): "95b1d7b65cf44e10b02ca7e6ccc5aaa7",
    (0, 3, 13, 0): "15ac649195d540cbbb0d2cd2c192860b",
    (0, 3, 13, 30): "241c0917bea0469db7cb2dd7faac5939",
    (0, 3, 14, 0): "39a3330cfc2748b886a77bb301faa783",
    (0, 3, 14, 30): "664e88f6103a469e9a9409b36b274aaf",
    (0, 3, 15, 0): "02d91522cb504af8acbebf70ffda4a5a",
    (0, 3, 15, 30): "22777b289d26459299a143e3069a1f45",
    (0, 3, 16, 0): "4c375a3ea5174765a2a10cb8bcc55123",
    (0, 3, 16, 30): "e98158a52bb545a1ad4d27abe2e4bedf",
    (0, 3, 17, 0): "b012bfef1d4043a6bd926b6c269604fe",
    (0, 3, 17, 30): "7bca758edabc4bb7b0e4983ed45ff903",
    (0, 3, 18, 0): "dc6265c0cd1742aea0ab84fc26ae57fc",
    (0, 3, 18, 30): "0b1fb31754944ba6b71bbd17d7317547",
    (0, 3, 19, 0): "b4377beb300a4d33a7b1eccfcc4f1d7f",
    (0, 3, 19, 30): "3a2f487f163c46beb0d20dddfd98a48e",
    (0, 3, 20, 0): "c9e7d22ccfb840648d39d2fc3dc430f5",
    (0, 3, 20, 30): "323d5efdbba84a7eb8111d075a1ede20",
    (0, 3, 21, 0): "e119e83aec3748698ac423e0904aca90",
    (0, 3, 21, 30): "bcc6928f320c4e6f9afbf6e93af752ba",
    (0, 3, 22, 0): "cb2df94052dc4554a6ddd35bfd5a65e1",
    (0, 3, 22, 30): "7a9fe689a33f42aa88e4d6cf5b5a7f25",
    (0, 3, 23, 0): "a39731ec63204334b23ad3f38653ae24",
    (0, 3, 23, 30): "e94ed809d40c49159396137f3de0d891",
    (0, 4, 4, 0): "7b3ab0d89973429eb97748da4d3ecc51",
    (0, 4, 4, 30): "9364f0408d0f419f8d18818686efd3c4",
    (0, 4, 5, 0): "02e919bfa84449dcadd21e092079f330",
    (0, 4, 5, 30): "14148f6e852649d28f9eef9b521b1470",
    (0, 4, 6, 0): "d165364063b44cb9ba6a92233e330ab0",
    (0, 4, 6, 30): "4cb63b1a4b0245f481a012d813c2b486",
    (0, 4, 7, 0): "081f1800284d4dffabc610759f168dfe",
    (0, 4, 7, 30): "fd96ebfd49dc47b888eb60ec488998c0",
    (0, 4, 8, 0): "b18fc2a73b274775b325b976800eb29c",
    (0, 4, 8, 30): "4a38b1036b314b62b39d97b03bee65f5",
    (0, 4, 9, 0): "fc1c8860df4d44df964d94365e12d2ee",
    (0, 4, 9, 30): "a2958aae827345f9a7862baca66e76f6",
    (0, 4, 10, 0): "74c85f660f2145a6942f465234babac2",
    (0, 4, 10, 30): "e5125c859e124b18a070cb733461be1f",
    (0, 4, 11, 0): "c5b8e1cb438f4b10ae8ba1585cfef073",
    (0, 4, 11, 30): "e14993b25e084149a09d9246ecb8daca",
    (0, 4, 12, 0): "3117dcfb61d241358985b339678a026a",
    (0, 4, 12, 30): "7fbfd59ab881417eb10c69a76406eaf5",
    (0, 4, 13, 0): "4f1745429c6242ae8a51052ede24b18c",
    (0, 4, 13, 30): "132646f5717149c7bf75f607fd7b37a9",
    (0, 4, 14, 0): "27e0e2bb416449af810a3edff87dab99",
    (0, 4, 14, 30): "b0400b884225471b9badeb7a8ec605d2",
    (0, 4, 15, 0): "d70a44ceaa824a05b876ef5a97b52458",
    (0, 4, 15, 30): "d8a2cfbbd38d43a382c7a33d365f40aa",
    (0, 4, 16, 0): "c5d9ad416529422794dd43f83408420c",
    (0, 4, 16, 30): "b19c7e56c0364b61bc8b12b784a101e9",
    (0, 4, 17, 0): "564c07df3137424b9c8cf6c2d4dc553e",
    (0, 4, 17, 30): "71f8897632e94245b56e5af2668cbf0a",
    (0, 4, 18, 0): "92c048289e814818bcf81a97809db805",
    (0, 4, 18, 30): "cb507c90e0a8431a860eb2d300b5aeff",
    (0, 4, 19, 0): "e8e7e5ac4ab9494b886fd8a7162966b7",
    (0, 4, 19, 30): "24ccb006ab55462ab623231e4540bdc5",
    (0, 4, 20, 0): "46c4f02e65424556a5a9913d3da5dcc5",
    (0, 4, 20, 30): "0aade5a6b98c47428d0c38bff9de909d",
    (0, 4, 21, 0): "dbdbf8d05e7647f09eb18576091a4d6e",
    (0, 4, 21, 30): "17385a2edfb940f284b286025dae49f9",
    (0, 4, 22, 0): "3997816621f14ab19564d64eb4a0e2e5",
    (0, 4, 22, 30): "fa433939db5746038cdd60fbf1ccfe0d",
    (0, 4, 23, 0): "c5f45ab046ce4f10a761f3df102622b3",
    (0, 4, 23, 30): "c5a44df18ee3451383e94a621b68e43f",
    (0, 5, 4, 0): "27aa8cd5b12e47b185cdec0dd8ef8e28",
    (0, 5, 4, 30): "8ba3f297ca034757b5b91da79cdd1845",
    (0, 5, 5, 0): "22167d6945c240bda1ba62eff06a465f",
    (0, 5, 5, 30): "5a1dd9df1bb746a8ba6f1873a2632ca9",
    (0, 5, 6, 0): "8045b59b488749ae83c12f976df45c9a",
    (0, 5, 6, 30): "fde3dfc40d0e4d988eb9bfe9ab83b9b1",
    (0, 5, 7, 0): "88b7292887e348b9b499f37246504417",
    (0, 5, 7, 30): "dc451666f3554d09900f9122c97081e6",
    (0, 5, 8, 0): "89a965573fed45f9adac27e141fdc72a",
    (0, 5, 8, 30): "f90b8e6c6fc0443ea261406e9124b599",
    (0, 5, 9, 0): "82cec529d80d452286f28947db39e208",
    (0, 5, 9, 30): "a423f67dcedc4cd0bb37821b191b3e97",
    (0, 5, 10, 0): "31290fb7b5d0402da546ac34406d810a",
    (0, 5, 10, 30): "c2cf79fdd4064aeb877e8fc41ab1b902",
    (0, 5, 11, 0): "ac03c1b746c14ed1ae61604a35a7d1bd",
    (0, 5, 11, 30): "d64924e4177a4e64a1069b0a995a5f77",
    (0, 5, 12, 0): "088865a13f9a4e91b4b2787a93866bf0",
    (0, 5, 12, 30): "c890a92d5370400a988a7ee813a5ad85",
    (0, 5, 13, 0): "ca1d8b94d5c44e79a05e255c346452c6",
    (0, 5, 13, 30): "c5f8341f8d0e43afb0d881d9f9aa74e5",
    (0, 5, 14, 0): "ad221eb3d4ca4c6e846111ba43253541",
    (0, 5, 14, 30): "1b830a5b6d5247d28c8ea7916ee8d7df",
    (0, 5, 15, 0): "5af61a1fecb04747bc17d879d96f8030",
    (0, 5, 15, 30): "e1f6fa356a17457788394fefc624ce78",
    (0, 5, 16, 0): "e1f6fa356a17457788394fefc624ce78",
    (0, 5, 16, 30): "76230c1a18084684ac2337a2dbcd597e",
    (0, 5, 17, 0): "5d49bb0ab2cb4c1b85c701505a74eee9",
    (0, 5, 17, 30): "8c2f450cbc054e3389febc3af466733a",
    (0, 5, 18, 0): "ce568b41032445219a4e618b08e5771a",
    (0, 5, 18, 30): "f319597a4e8640f1bd54bfab553fad40",
    (0, 5, 19, 0): "50bb7a9d50ff476c9aad9cfd3444cf2c",
    (0, 5, 19, 30): "2d36a285ce9947f89ce89d66b1e50033",
    (0, 5, 20, 0): "6243095b55674700a02b90869f01ccad",
    (0, 5, 20, 30): "2b45e404f16e46768f367832311ade1b",
    (0, 5, 21, 0): "a660cddbb32c4131b400dad9adb57376",
    (0, 5, 21, 30): "f17a4d777ec84cbdb9ce3d0ceee8d2d6",
    (0, 5, 22, 0): "48ffce706a1d43508dfd4773c463dfa5",
    (0, 5, 22, 30): "3edc29592665484d859c2912d73f9ad2",
    (0, 5, 23, 0): "8c9192c1abd5403fb048b79bab743542",
    (0, 5, 23, 30): "39059d16671347789d957d4186531862",
    (0, 6, 4, 0): "f86aaa953c8d469087c9767f8b6752c4",
    (0, 6, 4, 30): "c5bfc5155d22459295268277f0b8ae54",
    (0, 6, 5, 0): "069173cb2bc24f51baa894526ceb8e3e",
    (0, 6, 5, 30): "9c0c3da93c3240dc8ba7ad6de8072d6d",
    (0, 6, 6, 0): "75b25b73076f4d9ea06b72555b8c225f",
    (0, 6, 6, 30): "6cb4a6511ef94238aea4b5f1aa323441",
    (0, 6, 7, 0): "a76637f5a6f34adaaa0874e7249e2833",
    (0, 6, 7, 30): "4ff4b292e2494f98873d88902948aaf7",
    (0, 6, 8, 0): "cf5d6a4618e245dd8895d9fb29aac980",
    (0, 6, 8, 30): "7b9eb75f070249a08f98d77a1b007f7b",
    (0, 6, 9, 0): "2b37816d76454b4eac3fa1e18587e3b3",
    (0, 6, 9, 30): "84da92a07e474b72bab5a3d2944c5360",
    (0, 6, 10, 0): "d9bd5d151a4d40b4934a03ef5716a10f",
    (0, 6, 10, 30): "e889cd8e6966450096c5198784bccea8",
    (0, 6, 11, 0): "638a650f54084869ab12532517f4585e",
    (0, 6, 11, 30): "881aff2c45c1489588efdda470229689",
    (0, 6, 12, 0): "17cc51c927fa4c1fb7864e490e2ec0ad",
    (0, 6, 12, 30): "ae873a558f6a4d36a19e675456ae85d9",
    (0, 6, 13, 0): "22780d67e9f3432ab194da4764b83a00",
    (0, 6, 13, 30): "ce677fa57c4045c5906f34e4ba45b474",
    (0, 6, 14, 0): "50fe6841c4db4ff79402fb4dda924a36",
    (0, 6, 14, 30): "ed09c925f08949b7996ad3f9ab834519",
    (0, 6, 15, 0): "7d40d5b777ce4c2086353c77fbe2a5ce",
    (0, 6, 15, 30): "aae385fc16544754bbb1b30e995fd2e0",
    (0, 6, 16, 0): "e174dd0b9d0844548a6829e5cce7c777",
    (0, 6, 16, 30): "93c270204ef24f48935a0c98c1adcb58",
    (0, 6, 17, 0): "157180de4ee14c89a2f1b8d853154a8c",
    (0, 6, 17, 30): "f278ea3135994676a46619d9638e3ed8",
    (0, 6, 18, 0): "ed391236a2784f289f968f7173513bf1",
    (0, 6, 18, 30): "4a2d5e71efbe4767a11e8b600e6cac09",
    (0, 6, 19, 0): "f18f57f521a64ca99dd9a6e2dba049bf",
    (0, 6, 19, 30): "457395ba8abc4cd98e94e8fd04e6fda4",
    (0, 6, 20, 0): "b3f603d610c5452f9aeb32fcc27c388a",
    (0, 6, 20, 30): "5d43291a391049e38a2fcaeeea91fd25",
    (0, 6, 21, 0): "32f0b283f84f431a9695e1304c31b9b8",
    (0, 6, 21, 30): "3dd30591f7424b9db7b4a0f299896602",
    (0, 6, 22, 0): "c458d4af04f84fc5b1e4fc17cae77243",
    (0, 6, 22, 30): "1b75f9c47395433a8f7207eb1491504e",
    (0, 6, 23, 0): "f7dd1a58472047a0aaf75df11f7f92c0",
    (0, 6, 23, 30): "1745588771ee4c95b78de0cd8504ea50",
    (0, 7, 4, 0): "1380b0542d14438fa789b0f60f127e93",
    (0, 7, 4, 30): "a7c4486266304400832a561c8361e8db",
    (0, 7, 5, 0): "8a782e2e6b0f46e38a4633e46d9a5270",
    (0, 7, 5, 30): "62483d0fedde41fc808570498c18369c",
    (0, 7, 6, 0): "3875505509ce4b468b22e88030b8441e",
    (0, 7, 6, 30): "c85bd471cfd74d30a65d018a80dc1bd9",
    (0, 7, 7, 0): "a5c0892b2ef6458f8a1c5f228b17daa4",
    (0, 7, 7, 30): "bd0c07591c054340ad022dd0c85116dc",
    (0, 7, 8, 0): "fa54fac2131647068402783e07df7622",
    (0, 7, 8, 30): "9ed9271f89634a1f8883bfb5c20ddfa9",
    (0, 7, 9, 0): "252c5a36c54646edb94b694528c7b840",
    (0, 7, 9, 30): "298bc2c3dee24e7ca4a7c7dd495d7436",
    (0, 7, 10, 0): "1f10e4799675447ab99863be592ed9ed",
    (0, 7, 10, 30): "294bf45cc76544dfb194fd7d4ac35bfd",
    (0, 7, 11, 0): "3e83ffdb83104556934992b677d562f5",
    (0, 7, 11, 30): "35ab77b4145245e08c4a836ffefb38e1",
    (0, 7, 12, 0): "3211e6cba19f4c38b4626e1c49246061",
    (0, 7, 12, 30): "3d54a65aff9e4a9fae698cd2ca7cc2ae",
    (0, 7, 13, 0): "2823997d676f4e3896c49b0d7c39789f",
    (0, 7, 13, 30): "ffa7c0a0a0bb4efd888828215abfd98b",
    (0, 7, 14, 0): "40831a708b944ffc80cb99fd5c5ff76a",
    (0, 7, 14, 30): "5e4756aaecd64a7aafecc23d8af188ca",
    (0, 7, 15, 0): "fbb41624cc9b4a429a6b751839911640",
    (0, 7, 15, 30): "caf8347bc3a54206a25206bdc404b94b",
    (0, 7, 16, 0): "f0b6911457834fe5b054e01cfc8a4226",
    (0, 7, 16, 30): "52625421413845c5b76bf08d4af4b1df",
    (0, 7, 17, 0): "8cf31635674b47309edf2e6171bdd399",
    (0, 7, 17, 30): "6ca03466f5d745568d98689d803ec2e8",
    (0, 7, 18, 0): "e6901b4adc0243838a5adacf6229fddf",
    (0, 7, 18, 30): "68b98418c1dd4f6080cf2b740051e5b9",
    (0, 7, 19, 0): "37713502fb854844acc5772f914b3d90",
    (0, 7, 19, 30): "1b99ce198e904a949c686d63b8af9372",
    (0, 7, 20, 0): "611a6fe4f63c478a8d4f20dfa7c59411",
    (0, 7, 20, 30): "e61d3adeda2944d9bbbe9d5aa920010a",
    (0, 7, 21, 0): "2db4c2cf66fc4383b34dc0ee92f9bd96",
    (0, 7, 21, 0): "2db4c2cf66fc4383b34dc0ee92f9bd96",
    (0, 7, 21, 30): "37ae9a3256534a81a82e20576ad47c00",
    (0, 7, 22, 0): "4b1092a0ec6f42019dba22ece5fa4737",
    (0, 7, 22, 30): "2724aac46384482dbcd234e14486eca4",
    (0, 7, 23, 0): "1ed467f7ec4d4fe6875d296c97891595",
    (0, 7, 23, 30): "961ac5a24d99425fab0cd21b065dcd3c",
}

# 0) update date
from notion_client import Client

# selenium steps
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

notion = Client(auth="secret_fdf83SxJcqjaOfkyt8bz0CUfZt63ziydbVAbNRa1a48")

# update = {'rich_text': [{'type': 'mention',
#                          'mention': {'type': 'date',
#                                      'date': {'start': '2023-03-03T06:00:00.000+01:00',
#                                               'end': None,
#                                               'time_zone': None}},
#                          'annotations': {'bold': True,
#                                          'italic': False,
#                                          'strikethrough': False,
#                                          'underline': False,
#                                          'code': False,
#                                          'color': 'default'},
#                          'plain_text': '2023-01-27T06:00:00.000+01:00',
#                          'href': None},
#                         {'type': 'text',
#                          'text': {'content': ' \n', 'link': None},
#                          'annotations': {'bold': True,
#                                          'italic': False,
#                                          'strikethrough': False,
#                                          'underline': False,
#                                          'code': False,
#                                          'color': 'default'},
#                          'plain_text': ' \n',
#                          'href': None}],
#           'checked': False,
#           'color': 'default'}

# notion.blocks.update(id, to_do=update)

# 1) get page
firefox_opts = Options()
firefox_opts.add_argument("-profile")
firefox_opts.add_argument("/home/isaac/.mozilla/firefox/uxoqb3lu.default-release")

firefox = webdriver.Firefox(options=firefox_opts)

firefox.get("https://www.notion.so/isaacriley/Schedule-10e2a531d36341da85f85410a07749de")

# # 2) find day & expand
# toggle = firefox.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div[21]/div/div[1]")
# firefox.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div[21]/div/div[1]").click()

# # 3) find time & click
# firefox.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div[21]/div/div[2]/div[2]/div/div[4]/div/div[2]/div[1]/div/span[1]/span[2]/span[2]").click()
# t = firefox.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div[21]/div/div[2]/div[2]/div/div[4]/div/div[2]/div[1]/div/span[1]/span[2]/span[2]").text

# #4) find new time & click
# firefox.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]").click()
# firefox.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div").click()
# firefox.find_element(By.XPATH, "//body").send_keys(Keys.ESCAPE)

REMIND_BUTTON1 = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]"
REMIND_BUTTON2 = "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div"

DATE_FORMAT_TIMEZONE_BUTTON = "/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[4]"
DATE_FORMAT_BUTTON = "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div"  # "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div"#"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div"#"/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div"

RELATIVE_BUTTON = "/html/body/div[1]/div/div[2]/div[4]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[5]/div/div/div"
#
TIME_FORMAT_BUTTON = (
    "/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div"
)
#                "/html/body/div[1]/div/div[2]/div[4]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div"
HOUR_24_BUTTON = "/html/body/div[1]/div/div[2]/div[4]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div"

# path1 = "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div[21]/div/div[2]/div[2]/div/div[4]/div/div[2]/div[1]/div/span[1]/span[2]/span[2]"
# path2 = "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div[21]/div/div[2]/div[2]/div/div[5]/div[1]/div[2]/div[1]/div/span[1]"

DAY_TOGGLES = {
    (-1, 5): "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[1]/div/div[1]/div",
    (-1, 6): "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[2]/div/div[1]/div",
    (-1, 7): "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[3]/div/div[1]/div",
    (0, 1): "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[4]/div/div[1]/div",
    (0, 2): "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[5]/div/div[1]/div",
    (0, 3): "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[6]/div/div[1]/div",
    (0, 4): "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[7]/div/div[1]/div",
    (0, 5): "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[8]/div/div[1]/div",
    (0, 6): "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[9]/div/div[1]/div",
    (0, 7): "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[10]/div/div[1]/div",
}


def get_xpath(week: int, day: int, hour: int, minute: int) -> str:
    div_day = int(day - 4 if week == -1 else day + 3)
    div_time = 2 * (hour - 3) - int(minute == 0)
    return f"/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/main/div[1]/div/div/div/div/div[{div_day}]/div/div[2]/div[2]/div/div[{div_time}]/div/div[2]/div[1]/div/span[1]/span[2]/span[2]"


# week, day, hour, minute = 0, 7, 22, 30
# xp = get_xpath(week, day, hour, minute)
# firefox.find_element(By.XPATH, DAY_TOGGLES[(week, day)]).click()
# firefox.find_element(By.XPATH, xp).click()
# firefox.find_element(By.XPATH, REMIND_BUTTON1).click()
# firefox.find_element(By.XPATH, REMIND_BUTTON2).click()
# firefox.find_element(By.XPATH, "//body").send_keys(Keys.ESCAPE)
today = date.today()
today_weekday = today.isoweekday()
today_ordinal = today.toordinal()


def filt(k):
    return k[0] == (-1 if today_weekday in {1, 2, 3, 4} else 0)


def fix_date(date_str: str, day) -> str:
    pydate = date.fromisoformat(date_str[:10])
    ordinal = pydate.toordinal()
    next_day = today_ordinal + (day - today_weekday) % 7
    new_date = date.fromordinal(next_day)
    print(pydate, day, ordinal, next_day, new_date)
    return str(new_date) + date_str[10:]


def pause():
    time.sleep(0.3 + random.random())


def minipause():
    time.sleep(0.1 + 0.5 * random.random())


def longpause():
    time.sleep(3 + random.random())


def main():
    # # change dates
    # for k, v in filter(lambda x: filt(x[0]), TIME_BLOCK_IDS.items()):
    # #for k, v in list(filter(lambda x: filt(x[0]), TIME_BLOCK_IDS.items()))[10:]:
    # #for k, v in [((-1, 5, 21, 0), "3c0550979bec4333a4cfe6c9e34f2e03")]:
    #     week, day, hour, minute = k
    #     print(k)
    #     minipause()
    #     new_to_do = notion.blocks.retrieve(v)["to_do"]
    #     d = new_to_do["rich_text"][0]["mention"]["date"]["start"]
    #     new_d = fix_date(d, day)
    #     new_to_do["rich_text"][0]["mention"]["date"]["start"] = new_d
    #     new_to_do["rich_text"][0]["plain_text"] = new_d

    #     print(d)
    #     print(new_to_do)
    #     minipause()
    #     u = notion.blocks.update(v, to_do=new_to_do)

    # close open toggles
    for week, day in DAY_TOGGLES.keys():
        print(week, day)
        try:
            pause()
            print(".")
            firefox.find_element(By.XPATH, get_xpath(week, day, 8, 30))
            pause()
            print("..")
            firefox.find_element(By.XPATH, DAY_TOGGLES[(week, day)]).click()
            print("...")
        except:
            pass

    for week, day in filter(filt, DAY_TOGGLES.keys()):
        print(week, day, "===========================================")
        pause()
        firefox.find_element(By.XPATH, DAY_TOGGLES[(week, day)]).click()
        for hour in range(4, 7):
            print(hour, "-----------------------------------------")
            for minute in (0, 30):
                longpause()
                firefox.find_element(By.XPATH, get_xpath(week, day, hour, minute)).click()
                longpause()
                firefox.find_element(By.XPATH, REMIND_BUTTON1).click()
                longpause()
                firefox.find_element(By.XPATH, REMIND_BUTTON2).click()
                longpause()

                firefox.find_element(By.XPATH, DATE_FORMAT_TIMEZONE_BUTTON).click()
                longpause()
                firefox.find_element(By.XPATH, DATE_FORMAT_BUTTON).click()
                longpause()
                firefox.find_element(By.XPATH, RELATIVE_BUTTON).click()
                longpause()

                firefox.find_element(By.XPATH, TIME_FORMAT_BUTTON).click()
                longpause()
                firefox.find_element(By.XPATH, HOUR_24_BUTTON).click()
                longpause()
                firefox.find_element(By.XPATH, "//body").send_keys(Keys.ESCAPE)
                longpause()
                firefox.find_element(By.XPATH, "//body").send_keys(Keys.ESCAPE)
                longpause()
                firefox.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div").click()
                longpause()
        firefox.find_element(By.XPATH, DAY_TOGGLES[(week, day)]).click()
