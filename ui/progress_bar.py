'Manage the progressbar of the UI.'
import asyncio,js
class ProgressBar:
	'Management for the Progress Bar of the UI.'
	def __init__(A):'Control the function of the progressbar.';A.modal="$('#progressmodal')";A.status="$('#progress-text')";A.bar="$('#patchprogress')"
	async def update_progress(A,val,text):
		'Update your progress percentage and text.\n\n        Args:\n            val (int): Percent of 100.\n            text (str): Text to display.\n        ';B=val
		if B==0:A._show();A._width(B);A._text(text)
		else:await asyncio.sleep(3);A._show();A._width(B);A._text(text)
	async def reset(A):
		'Set hide, text, width and added classes of the progressbar to nil.';await asyncio.sleep(7);A._hide();A._width(0);A._text('')
		for B in js.document.getElementById('patchprogress').classList:
			if'progress'not in B:A.set_class(B)
	def _width(A,val):
		'Set width to value converted to percentage.\n\n        Args:\n            val (int): Value percentage of 100.\n\n        Raises:\n            Exception: Raises an exception when number is outside 0-100\n        '
		if not 0<=val<=100:raise Exception('Width can only be 0-100')
		B=val/10;C=B*100;js.eval(A.bar+f".width('{C}%')")
	def _text(A,text):
		'Set the text of the progress bar.\n\n        Args:\n            text (str): Text to set.\n        '
		try:B=text.replace("'",'"');js.eval(A.status+f".text('{B}')")
		except Exception:pass
	def _hide(A):'Hide the Modal.';js.eval(A.modal+".modal('hide')")
	def _show(A):'Show the Modal.';js.eval(A.modal+".modal('show')")
	def set_class(A,css):
		'Add or Remove the CSS class defined.\n\n        Args:\n            css (str): Class to add.\n        ';B=css
		def C():js.eval(A.bar+f".removeClass('{B}')")
		def D():js.eval(A.bar+f".addClass('{B}')")
		if js.eval(A.bar+f".hasClass('{B}')"):C()
		else:D()