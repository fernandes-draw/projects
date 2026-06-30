from django.db import models
from accounts.models import CustomUser


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name="CLIENTE")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.name


class ProductItem(models.Model):
    ref_mod = models.CharField(
        max_length=20, unique=True, verbose_name="REF. MOD")
    description = models.CharField(max_length=250, verbose_name="DESCRIÇÃO")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="items", verbose_name="CLIENTE")

    # Techinical parameters
    tooling_material = models.CharField(
        max_length=100, verbose_name="MATERIAL FERRAMENTAL")
    part_material = models.CharField(
        max_length=100, verbose_name="MATERIAL PEÇA")
    gross_weight = models.CharField(
        max_length=50, verbose_name="PESO BRUTO PEÇA")
    mold_cavities = models.IntegerField(verbose_name="FIGURAS MOLDES")
    box_quantity = models.CharField(max_length=50, verbose_name="QTDE CX")
    photo = models.ImageField(
        upload_to='items_photos/', blank=True, null=True, verbose_name="FOTO")

    class Meta:
        verbose_name = "Item do Produto"
        verbose_name_plural = "Itens do Produto"

    def __str__(self):
        return f"{self.ref_mod} - {self.description}"


class ProjectProcess(models.Model):
    STATUS_CHOICES = [
        ('montar_pasta', 'MONTAR PASTA USINAGEM'),
        ('aguardando_bloco', 'AGUARDANDO BLOCO'),
        ('em_usinagem', 'EM USINAGEM'),
        ('concluido', 'CONCLUÍDO'),
    ]

    item = models.OneToOneField(
        ProductItem, on_delete=models.CASCADE, related_name="process", verbose_name="ITEM")
    start_date = models.DateField(verbose_name="DATA INICIAL")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,
                              default='montar_pasta', verbose_name="SITUAÇÃO")
    responsible = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="RESP.")
    notes = models.TextField(blank=True, null=True, verbose_name="OBSERVAÇÕES")
    last_updated = models.DateTimeField(
        auto_now=True, verbose_name="DT. ÚLT. ALT.")

    class Meta:
        verbose_name = "Processo do Projeto"
        verbose_name_plural = "Processos do Projeto"

    def __str__(self):
        return f"Processo do Item: {self.item.ref_mod} - {self.get_status_display()}"
