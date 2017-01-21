# Parser.py

def get_results(json_text: 'json text') -> list:
    location_list = []
    for predictions in range(len(json_text['predictions'])):
        location_list.append(json_text['predictions'][predictions]['description'])
    return location_list
    
print(get_results({
   "predictions" : [
      {
         "description" : "Mission Viejo, CA, United States",
         "id" : "f4384df179c289b69ac72a1ab005e1f4093ee5d3",
         "matched_substrings" : [
            {
               "length" : 3,
               "offset" : 0
            }
         ],
         "place_id" : "ChIJm329k6_C3IARNEgxTpKFYic",
         "reference" : "CkQ4AAAAMG-lO7XOBHtCBrurQkstgtBBcvg-Glu5pge0Tx7ycJ7FQZcHWggYKGCVhGLJE2QjnPuxiKFPuLGRl8WcPafHmRIQ4NhRakqQ-z_tiUUCFtpCwRoUa_pfSw-AKQVKpryk5bJqTDyIwDg",
         "structured_formatting" : {
            "main_text" : "Mission Viejo",
            "main_text_matched_substrings" : [
               {
                  "length" : 3,
                  "offset" : 0
               }
            ],
            "secondary_text" : "CA, United States"
         },
         "terms" : [
            {
               "offset" : 0,
               "value" : "Mission Viejo"
            },
            {
               "offset" : 15,
               "value" : "CA"
            },
            {
               "offset" : 19,
               "value" : "United States"
            }
         ],
         "types" : [ "locality", "political", "geocode" ]
      },
      {
         "description" : "Mission Street, San Francisco, CA, United States",
         "id" : "6e231a9c8f361e438b5d68cdd554ad34f98fcbb7",
         "matched_substrings" : [
            {
               "length" : 3,
               "offset" : 0
            }
         ],
         "place_id" : "EjBNaXNzaW9uIFN0cmVldCwgU2FuIEZyYW5jaXNjbywgQ0EsIFVuaXRlZCBTdGF0ZXM",
         "reference" : "CkQ0AAAAWsB5pzN_3f1Q-AV2P1caZgMEifYFgVE9e7eKxBoMk5k7LYJBkh0VEHcwev1DcsR5ADviWAUvsT7zGp5VTVNpfxIQvM4EYnRQ1AjC24jNfjncMRoUu8vGmJZpubxEPHWlX8Fq9677w7M",
         "structured_formatting" : {
            "main_text" : "Mission Street",
            "main_text_matched_substrings" : [
               {
                  "length" : 3,
                  "offset" : 0
               }
            ],
            "secondary_text" : "San Francisco, CA, United States"
         },
         "terms" : [
            {
               "offset" : 0,
               "value" : "Mission Street"
            },
            {
               "offset" : 16,
               "value" : "San Francisco"
            },
            {
               "offset" : 31,
               "value" : "CA"
            },
            {
               "offset" : 35,
               "value" : "United States"
            }
         ],
         "types" : [ "route", "geocode" ]
      },
      {
         "description" : "Mission Drive, Solvang, CA, United States",
         "id" : "498b7a3e3f4dc570c9da0c89bed12a286835bfa8",
         "matched_substrings" : [
            {
               "length" : 3,
               "offset" : 0
            }
         ],
         "place_id" : "EilNaXNzaW9uIERyaXZlLCBTb2x2YW5nLCBDQSwgVW5pdGVkIFN0YXRlcw",
         "reference" : "CjQtAAAAKE8aaRAOPl24KhAxckBgWJW6maTiP0hH--twgAKOqS7ft4XyL9GQIKHRDeqXAUOKEhAPY_SrkV8_L3M6Nuu78gPzGhR7DtkmJynF2AKogyGvK9a7GFy2_Q",
         "structured_formatting" : {
            "main_text" : "Mission Drive",
            "main_text_matched_substrings" : [
               {
                  "length" : 3,
                  "offset" : 0
               }
            ],
            "secondary_text" : "Solvang, CA, United States"
         },
         "terms" : [
            {
               "offset" : 0,
               "value" : "Mission Drive"
            },
            {
               "offset" : 15,
               "value" : "Solvang"
            },
            {
               "offset" : 24,
               "value" : "CA"
            },
            {
               "offset" : 28,
               "value" : "United States"
            }
         ],
         "types" : [ "route", "geocode" ]
      },
      {
         "description" : "Mission Canyon Road, Santa Barbara, CA, United States",
         "id" : "b4ce3bbc7e65e3e0e76d3b5e2b7fb847585307dd",
         "matched_substrings" : [
            {
               "length" : 3,
               "offset" : 0
            }
         ],
         "place_id" : "EjVNaXNzaW9uIENhbnlvbiBSb2FkLCBTYW50YSBCYXJiYXJhLCBDQSwgVW5pdGVkIFN0YXRlcw",
         "reference" : "CkQ5AAAAPdpkjV5xkqiLmIYjtxaztyQnBQGzRXXMy62_Tdt5Qqrb3XHm92Tvr9l0ZUMsbNOcUhkivLCXxi-nbCEeS6Xs8hIQusrQzP-8-F4_xM75Ca3cpxoUPHlVOsKVko_9_w2SwAwVRnoWxUU",
         "structured_formatting" : {
            "main_text" : "Mission Canyon Road",
            "main_text_matched_substrings" : [
               {
                  "length" : 3,
                  "offset" : 0
               }
            ],
            "secondary_text" : "Santa Barbara, CA, United States"
         },
         "terms" : [
            {
               "offset" : 0,
               "value" : "Mission Canyon Road"
            },
            {
               "offset" : 21,
               "value" : "Santa Barbara"
            },
            {
               "offset" : 36,
               "value" : "CA"
            },
            {
               "offset" : 40,
               "value" : "United States"
            }
         ],
         "types" : [ "route", "geocode" ]
      },
      {
         "description" : "Old Mission Santa Barbara, Laguna Street, Santa Barbara, CA, United States",
         "id" : "d8bc6a1e890bd00b7a85fc4166e5e1b1011ecf4f",
         "matched_substrings" : [
            {
               "length" : 3,
               "offset" : 4
            }
         ],
         "place_id" : "ChIJA20zJYEU6YARZ_lTVZWZACI",
         "reference" : "CmRYAAAA8HCba8qAE53GlAwFf6h6rPb-ilFJ4Ln8801xcfhhAbPKHX1EB1f2kL45FQgLwLn0oBEs0ySDSFad2jxlQXrqcMWHEyaEm_tIv9hL8B2t177qq2y_Itp0ekM2oEHxcl14EhCxJjGEzVnEezQhpvHqTOJdGhQnkfPLmDSV1tcFj6fRSIXYT5RZPA",
         "structured_formatting" : {
            "main_text" : "Old Mission Santa Barbara",
            "main_text_matched_substrings" : [
               {
                  "length" : 3,
                  "offset" : 4
               }
            ],
            "secondary_text" : "Laguna Street, Santa Barbara, CA, United States"
         },
         "terms" : [
            {
               "offset" : 0,
               "value" : "Old Mission Santa Barbara"
            },
            {
               "offset" : 27,
               "value" : "Laguna Street"
            },
            {
               "offset" : 42,
               "value" : "Santa Barbara"
            },
            {
               "offset" : 57,
               "value" : "CA"
            },
            {
               "offset" : 61,
               "value" : "United States"
            }
         ],
         "types" : [ "establishment" ]
      }
   ],
   "status" : "OK"
}))