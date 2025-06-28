{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "34cab237-5623-4a37-87d2-a77b5765d74e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-28 21:57:05.925 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:05.928 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:05.929 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:05.929 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:05.930 WARNING streamlit.runtime.state.session_state_proxy: Session state does not function when running a script without `streamlit run`\n",
      "2025-06-28 21:57:05.931 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:06.690 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Admin\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-06-28 21:57:06.691 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:06.691 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:06.692 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:06.693 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:06.694 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:06.694 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:06.695 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 21:57:06.695 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "import streamlit as st\n",
    "user_input = st.text_area(\"Enter Your Email ID\")\n",
    "\n",
    "pattern = re.compile(r'([A-Za-z0-9]+[.])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+')\n",
    "\n",
    "def check(email):\n",
    "    if re.fullmatch(pattern, email):\n",
    "      return \"Valid email id\"\n",
    "    else:\n",
    "      return \"Invalid email id\"\n",
    "      \n",
    "if(st.button('Check')):\n",
    "    response = check(user_input)\n",
    "    st.success(response)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f3bbcaec-e812-477e-9422-99a1f2747feb",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3677453945.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[2], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit run stream.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run stream.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "337b5aa9-6199-4bbb-bae4-e72886248f63",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
