{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"Strings.ipynb","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyMaGtv7T8l1u0ZuFxLKwoS9"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":3,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"l8MiO48-aIcv","executionInfo":{"status":"ok","timestamp":1659775403737,"user_tz":180,"elapsed":15682,"user":{"displayName":"Alberto Ávalos","userId":"13798502889986312955"}},"outputId":"1344307a-2c10-4cfd-f0a0-5d21da1cef5d"},"outputs":[{"name":"stdout","output_type":"stream","text":["Digite algo: legal python\n"]}],"source":["a= input(\"Digite algo: \")"]},{"cell_type":"code","source":["print(a.upper())\n","# Transforma todas a letas em Maiúsculas\n","\n","print(a.lower()) \n","#Transforma todas as letas em minúsculas\n","\n","print(a.title())\n","#Transforma somente as iniciais em Maiúscula\n","\n","print(a.replace(\"python\",\"Filho\"))\n","#subtitui determinada palavra\n","\n","print(a.count(a))\n","#irá contar quantas frases que tem no conjunto, como neste somente temos o \"a\"\n","\n","print(len(a))\n","#conta o total de letras, Pode ser usado em vetores,matrizes ou strings\n","\n","print(a.find('o'))\n","#irá achar em que posição (Número) está essa letra\n","\n","print(a[4::-1])\n","#inverte conforme posição "],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"XWVPGwVMae3R","executionInfo":{"status":"ok","timestamp":1659775552836,"user_tz":180,"elapsed":260,"user":{"displayName":"Alberto Ávalos","userId":"13798502889986312955"}},"outputId":"72cfb0ce-eebd-4f7f-9b00-d1cbfbe3c918"},"execution_count":5,"outputs":[{"output_type":"stream","name":"stdout","text":["LEGAL PYTHON\n","legal python\n","Legal Python\n","legal Filho\n","1\n","12\n","10\n","lagel\n"]}]}]}