{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a63bf500",
   "metadata": {},
   "outputs": [
    {
     "ename": "OSError",
     "evalue": "Cannot save file into a non-existent directory: 'data'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mOSError\u001b[39m                                   Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[2]\u001b[39m\u001b[32m, line 33\u001b[39m\n\u001b[32m     31\u001b[39m df = pd.DataFrame(data)\n\u001b[32m     32\u001b[39m df = df.sample(frac=\u001b[32m1\u001b[39m).reset_index(drop=\u001b[38;5;28;01mTrue\u001b[39;00m)\n\u001b[32m---> \u001b[39m\u001b[32m33\u001b[39m \u001b[43mdf\u001b[49m\u001b[43m.\u001b[49m\u001b[43mto_csv\u001b[49m\u001b[43m(\u001b[49m\u001b[33;43m\"\u001b[39;49m\u001b[33;43mdata/emails.csv\u001b[39;49m\u001b[33;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mindex\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\n\u001b[32m     34\u001b[39m \u001b[38;5;28mprint\u001b[39m(\u001b[33m\"\u001b[39m\u001b[33mDataset saved to data/emails.csv\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\YASH SAMIR WADEKAR\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\util\\_decorators.py:333\u001b[39m, in \u001b[36mdeprecate_nonkeyword_arguments.<locals>.decorate.<locals>.wrapper\u001b[39m\u001b[34m(*args, **kwargs)\u001b[39m\n\u001b[32m    327\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(args) > num_allow_args:\n\u001b[32m    328\u001b[39m     warnings.warn(\n\u001b[32m    329\u001b[39m         msg.format(arguments=_format_argument_list(allow_args)),\n\u001b[32m    330\u001b[39m         \u001b[38;5;167;01mFutureWarning\u001b[39;00m,\n\u001b[32m    331\u001b[39m         stacklevel=find_stack_level(),\n\u001b[32m    332\u001b[39m     )\n\u001b[32m--> \u001b[39m\u001b[32m333\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[43m*\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43m*\u001b[49m\u001b[43m*\u001b[49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\YASH SAMIR WADEKAR\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\core\\generic.py:3967\u001b[39m, in \u001b[36mNDFrame.to_csv\u001b[39m\u001b[34m(self, path_or_buf, sep, na_rep, float_format, columns, header, index, index_label, mode, encoding, compression, quoting, quotechar, lineterminator, chunksize, date_format, doublequote, escapechar, decimal, errors, storage_options)\u001b[39m\n\u001b[32m   3956\u001b[39m df = \u001b[38;5;28mself\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(\u001b[38;5;28mself\u001b[39m, ABCDataFrame) \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;28mself\u001b[39m.to_frame()\n\u001b[32m   3958\u001b[39m formatter = DataFrameFormatter(\n\u001b[32m   3959\u001b[39m     frame=df,\n\u001b[32m   3960\u001b[39m     header=header,\n\u001b[32m   (...)\u001b[39m\u001b[32m   3964\u001b[39m     decimal=decimal,\n\u001b[32m   3965\u001b[39m )\n\u001b[32m-> \u001b[39m\u001b[32m3967\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mDataFrameRenderer\u001b[49m\u001b[43m(\u001b[49m\u001b[43mformatter\u001b[49m\u001b[43m)\u001b[49m\u001b[43m.\u001b[49m\u001b[43mto_csv\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m   3968\u001b[39m \u001b[43m    \u001b[49m\u001b[43mpath_or_buf\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3969\u001b[39m \u001b[43m    \u001b[49m\u001b[43mlineterminator\u001b[49m\u001b[43m=\u001b[49m\u001b[43mlineterminator\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3970\u001b[39m \u001b[43m    \u001b[49m\u001b[43msep\u001b[49m\u001b[43m=\u001b[49m\u001b[43msep\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3971\u001b[39m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3972\u001b[39m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[43m=\u001b[49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3973\u001b[39m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[43m=\u001b[49m\u001b[43mcompression\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3974\u001b[39m \u001b[43m    \u001b[49m\u001b[43mquoting\u001b[49m\u001b[43m=\u001b[49m\u001b[43mquoting\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3975\u001b[39m \u001b[43m    \u001b[49m\u001b[43mcolumns\u001b[49m\u001b[43m=\u001b[49m\u001b[43mcolumns\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3976\u001b[39m \u001b[43m    \u001b[49m\u001b[43mindex_label\u001b[49m\u001b[43m=\u001b[49m\u001b[43mindex_label\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3977\u001b[39m \u001b[43m    \u001b[49m\u001b[43mmode\u001b[49m\u001b[43m=\u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3978\u001b[39m \u001b[43m    \u001b[49m\u001b[43mchunksize\u001b[49m\u001b[43m=\u001b[49m\u001b[43mchunksize\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3979\u001b[39m \u001b[43m    \u001b[49m\u001b[43mquotechar\u001b[49m\u001b[43m=\u001b[49m\u001b[43mquotechar\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3980\u001b[39m \u001b[43m    \u001b[49m\u001b[43mdate_format\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdate_format\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3981\u001b[39m \u001b[43m    \u001b[49m\u001b[43mdoublequote\u001b[49m\u001b[43m=\u001b[49m\u001b[43mdoublequote\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3982\u001b[39m \u001b[43m    \u001b[49m\u001b[43mescapechar\u001b[49m\u001b[43m=\u001b[49m\u001b[43mescapechar\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3983\u001b[39m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[43m=\u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m   3984\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\YASH SAMIR WADEKAR\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\io\\formats\\format.py:1014\u001b[39m, in \u001b[36mDataFrameRenderer.to_csv\u001b[39m\u001b[34m(self, path_or_buf, encoding, sep, columns, index_label, mode, compression, quoting, quotechar, lineterminator, chunksize, date_format, doublequote, escapechar, errors, storage_options)\u001b[39m\n\u001b[32m    993\u001b[39m     created_buffer = \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[32m    995\u001b[39m csv_formatter = CSVFormatter(\n\u001b[32m    996\u001b[39m     path_or_buf=path_or_buf,\n\u001b[32m    997\u001b[39m     lineterminator=lineterminator,\n\u001b[32m   (...)\u001b[39m\u001b[32m   1012\u001b[39m     formatter=\u001b[38;5;28mself\u001b[39m.fmt,\n\u001b[32m   1013\u001b[39m )\n\u001b[32m-> \u001b[39m\u001b[32m1014\u001b[39m \u001b[43mcsv_formatter\u001b[49m\u001b[43m.\u001b[49m\u001b[43msave\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m   1016\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m created_buffer:\n\u001b[32m   1017\u001b[39m     \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(path_or_buf, StringIO)\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\YASH SAMIR WADEKAR\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\io\\formats\\csvs.py:251\u001b[39m, in \u001b[36mCSVFormatter.save\u001b[39m\u001b[34m(self)\u001b[39m\n\u001b[32m    247\u001b[39m \u001b[38;5;250m\u001b[39m\u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m    248\u001b[39m \u001b[33;03mCreate the writer & save.\u001b[39;00m\n\u001b[32m    249\u001b[39m \u001b[33;03m\"\"\"\u001b[39;00m\n\u001b[32m    250\u001b[39m \u001b[38;5;66;03m# apply compression and byte/text conversion\u001b[39;00m\n\u001b[32m--> \u001b[39m\u001b[32m251\u001b[39m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[43mget_handle\u001b[49m\u001b[43m(\u001b[49m\n\u001b[32m    252\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    253\u001b[39m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    254\u001b[39m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    255\u001b[39m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    256\u001b[39m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mcompression\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    257\u001b[39m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[43m=\u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[43m.\u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[43m,\u001b[49m\n\u001b[32m    258\u001b[39m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m handles:\n\u001b[32m    259\u001b[39m     \u001b[38;5;66;03m# Note: self.encoding is irrelevant here\u001b[39;00m\n\u001b[32m    260\u001b[39m     \u001b[38;5;28mself\u001b[39m.writer = csvlib.writer(\n\u001b[32m    261\u001b[39m         handles.handle,\n\u001b[32m    262\u001b[39m         lineterminator=\u001b[38;5;28mself\u001b[39m.lineterminator,\n\u001b[32m   (...)\u001b[39m\u001b[32m    267\u001b[39m         quotechar=\u001b[38;5;28mself\u001b[39m.quotechar,\n\u001b[32m    268\u001b[39m     )\n\u001b[32m    270\u001b[39m     \u001b[38;5;28mself\u001b[39m._save()\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\YASH SAMIR WADEKAR\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\io\\common.py:749\u001b[39m, in \u001b[36mget_handle\u001b[39m\u001b[34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[39m\n\u001b[32m    747\u001b[39m \u001b[38;5;66;03m# Only for write methods\u001b[39;00m\n\u001b[32m    748\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[33m\"\u001b[39m\u001b[33mr\u001b[39m\u001b[33m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m mode \u001b[38;5;129;01mand\u001b[39;00m is_path:\n\u001b[32m--> \u001b[39m\u001b[32m749\u001b[39m     \u001b[43mcheck_parent_directory\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;28;43mstr\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mhandle\u001b[49m\u001b[43m)\u001b[49m\u001b[43m)\u001b[49m\n\u001b[32m    751\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m compression:\n\u001b[32m    752\u001b[39m     \u001b[38;5;28;01mif\u001b[39;00m compression != \u001b[33m\"\u001b[39m\u001b[33mzstd\u001b[39m\u001b[33m\"\u001b[39m:\n\u001b[32m    753\u001b[39m         \u001b[38;5;66;03m# compression libraries do not like an explicit text-mode\u001b[39;00m\n",
      "\u001b[36mFile \u001b[39m\u001b[32mc:\\Users\\YASH SAMIR WADEKAR\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\pandas\\io\\common.py:616\u001b[39m, in \u001b[36mcheck_parent_directory\u001b[39m\u001b[34m(path)\u001b[39m\n\u001b[32m    614\u001b[39m parent = Path(path).parent\n\u001b[32m    615\u001b[39m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m parent.is_dir():\n\u001b[32m--> \u001b[39m\u001b[32m616\u001b[39m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mOSError\u001b[39;00m(\u001b[33mrf\u001b[39m\u001b[33m\"\u001b[39m\u001b[33mCannot save file into a non-existent directory: \u001b[39m\u001b[33m'\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mparent\u001b[38;5;132;01m}\u001b[39;00m\u001b[33m'\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[31mOSError\u001b[39m: Cannot save file into a non-existent directory: 'data'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import random\n",
    "\n",
    "hr_emails = [\n",
    "    \"Can I get my salary slip for last month?\",\n",
    "    \"I want to apply for a leave next week.\",\n",
    "    \"Is there an update on the holiday calendar?\",\n",
    "    \"How can I update my bank details for salary?\"\n",
    "]\n",
    "\n",
    "it_emails = [\n",
    "    \"My laptop is not turning on, need help.\",\n",
    "    \"The VPN connection is not working.\",\n",
    "    \"I forgot my system password.\",\n",
    "    \"Outlook is crashing frequently.\"\n",
    "]\n",
    "\n",
    "other_emails = [\n",
    "    \"When is the next company townhall?\",\n",
    "    \"Who is the point of contact for facility management?\",\n",
    "    \"Where can I find the new cafeteria menu?\",\n",
    "    \"There is a cleanliness issue in the restroom.\"\n",
    "]\n",
    "\n",
    "data = []\n",
    "for i in range(100):\n",
    "    data.append({\"email_text\": random.choice(hr_emails), \"category\": \"HR\"})\n",
    "    data.append({\"email_text\": random.choice(it_emails), \"category\": \"IT\"})\n",
    "    data.append({\"email_text\": random.choice(other_emails), \"category\": \"Other\"})\n",
    "\n",
    "df = pd.DataFrame(data)\n",
    "df = df.sample(frac=1).reset_index(drop=True)\n",
    "df.to_csv(\"data\\emails.csv\", index=False)\n",
    "print(\"Dataset saved to data/emails.csv\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
